import os
import io
import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd


def get_table_headers(table):
    table_headers = []
    # the first tr contain the column headers
    # skip the first "column header" because it's blank and for the row ids we are not keeping
    for th in table.find("tr").find_all("th")[1:]:
        table_headers.append(th.text.strip().lower().replace(" ", "_"))
    return table_headers


def get_table_rows(table):
    table_rows = []
    # skip the first tr as that was the column header
    for tr in table.find_all("tr")[1:]:
        # skip the first column in each row as it is a row number
        tds = tr.find_all("td")[1:]
        cells = []
        for td in tds:
            cells.append(td.text.strip())
        table_rows.append(cells)
    return table_rows


def get_nrevss_data(url_bases, url_ext, locations, location_name=None, folder_path="auxiliary-data/nrevss/"):
    today = date.today()
    today_str = today.strftime("%Y-%m-%d")

    for u in url_bases:
        headers = []
        rows = []
        filename = ""

        for location in locations:
            if location_name is None:
                loc_name = location
            else:
                loc_name = location_name
            try:
                r = requests.get(u + location + url_ext)
                if r.status_code == 200:

                    # parse the html
                    soup = BeautifulSoup(r.text, 'html.parser')

                    # search for the <table> tags
                    tables = soup.find_all("table")

                    for t in tables:
                        filename = (t.caption.text.strip().replace("for " + loc_name, "").
                                    replace("Insufficient Antigen Data:  ", "").
                                    replace("Insufficient Data:  ", "").lower().
                                    replace(" ", "_").replace("(", "").replace(")", "") + ".csv")
                        headers = get_table_headers(t)
                        state_rows = get_table_rows(t)
                        rows.extend(state_rows)

                else:
                    print("Error getting page; HTTP status " + str(r.status_code))

            except Exception as e:
                print("Error for state " + location + " and URL " + u + location + url_ext)
                print(e)

        # Add date information
        df = pd.DataFrame(rows)
        df = df.rename(columns=dict(zip(range(len(headers)), headers)))
        df["repweekdate"] = pd.to_datetime(df["repweekdate"]).dt.strftime("%Y-%m-%d")
        df["as_of"] = today_str

        file_dir = folder_path + filename
        if os.path.isfile(file_dir):
            df0 = pd.read_csv(file_dir)
            df_ts = set(list(df["repweekdate"].drop_duplicates())).intersection(
                list(df0["repweekdate"].drop_duplicates()))
            df0 = df0[~df0["repweekdate"].isin(df_ts)]
            df_all = pd.concat([df0, df], ignore_index=True)
        else:
            df_all = df
        # write the csv file
        df_all.to_csv(file_dir, index=False)


# RSV State Trends - The National Respiratory and Enteric Virus Surveillance System (NREVSS)
state_bases = [
    "https://www.cdc.gov/surveillance/nrevss/images/rsvstate/RSV1PPCent3AVG_State",
    "https://www.cdc.gov/surveillance/nrevss/images/rsvstate/RSV4PPCent3AVG_State",
    "https://www.cdc.gov/surveillance/nrevss/images/rsvstate/RSV14NumCent5AVG_State"]
hub_locations = pd.read_csv("data-locations/locations.csv")
states = list(hub_locations["abbreviation"])
to_remove = ["AS", "GU", "MP", "PR", "UM", "VI", "US"]
for i in to_remove:
    states.remove(i)
get_nrevss_data(state_bases, ".htm", states)

# RSV National Trends - The National Respiratory and Enteric Virus Surveillance System (NREVSS)
nat_bases = {"https://www.cdc.gov/surveillance/nrevss/images/trend_images/RSV124PP_",
             "https://www.cdc.gov/surveillance/nrevss/images/trend_images/RSV14Num_"}
get_nrevss_data(nat_bases, ".htm", ["Nat"], location_name="the ")

# Weekly Rates of Laboratory-Confirmed RSV Hospitalizations - Respiratory Syncytial Virus Hospitalization
# Surveillance Network (RSV-NET)
res = requests.get("https://data.cdc.gov/api/views/29hc-w46k/rows.csv?accessType=DOWNLOAD")
df_rsvnet = pd.read_csv(io.StringIO(res.text),
                        dtype={'State': "string", 'Season': "string", 'MMWR Week': "string",
                               'Week ending date': "string", 'Age Category': "string",
                               'Sex': "string", 'Race': "string", 'Rate': "float",
                               'Cumulative Rate': "float"})
df_rsvnet.to_csv("auxiliary-data/rsv-net/weekly_rates_lab_confirmed_rsv_hosp.csv")