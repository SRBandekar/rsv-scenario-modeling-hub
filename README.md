# RSV Scenario Modeling Hub

## Rationale    

Even the best models of infectious disease transmission struggle to give 
accurate forecasts at time scales greater than 3-4 weeks due to unpredictable 
drivers like changing policy environments, behavior change, development of new 
control measures, and stochastic events. However, policy decisions around the 
course of infectious diseases, particularly emerging and seasonal infections, 
often require projections in the time frame of months. The goal of long-term 
projections is to compare outbreak trajectories under different scenarios, as 
opposed to offering a specific, unconditional estimate of what “will” happen. 
As such, long-term projections can guide longer-term decision-making while 
short-term forecasts are more useful for situational awareness and guiding 
immediate response.

We have specified a set of scenarios and target outcomes to allow alignment of 
model projections for collective insights. Scenarios have been designed in 
consultation with academic modeling teams and government agencies (e.g., CDC).

This repository follows the guidelines and standards outlined by the 
[hubverse](https://hubdocs.readthedocs.io/), 
which provides a set of data formats and open source tools for modeling hubs.

## How to participate    

The RSV Scenario Modeling Hub is open to any team willing to provide projections
at the right temporal and spatial scales, with minimal gatekeeping. We only 
require that participating teams share point estimates and uncertainty bounds, 
along with a short model description and answers to a list of key questions 
about design. A major output of the projection hub is ensemble estimates of 
epidemic outcomes (e.g., infection, hospitalizations, and deaths), for different
time points, intervention scenarios, and US jurisdictions.

Those interested to participate, please read the README file and email us at 
scenariohub@midasnetwork.us .

Model projections should be submitted via pull request to the 
[model-output/](./model-output/) folder and associated metadata should be 
submitted at the same time to the [model-metadata/](./model-metadata/) folder 
of this GitHub repository. 
Technical instructions for submission and required file formats can be found 
[here](./model-output/README.md) and 
[here, for the metadata file](./model_metadata/README.md)

## Target data

The [target-data/](./target-data/) folder contains the RSV hospitalization data
(also called "truth data") standardized from the 
[Weekly Rates of Laboratory-Confirmed RSV Hospitalizations from the RSV-NET Surveillance System](https://data.cdc.gov/Public-Health-Surveillance/Weekly-Rates-of-Laboratory-Confirmed-RSV-Hospitali/29hc-w46k).

The weekly hospitalization number per location are going to be used as truth 
data in the hub.

## Auxiliary Data

The repository stores and updates additional data relevant to the RSV modeling 
efforts:

- Population and census data:
    - National and State level name and fips code as used in the Hub and
    associated population size.
    - State level population size per year and per age from the US Census 
    Bureau.

- Birth Rate:
    - Birth Number and Rate per state and per year from 1995 to 2022 included.
    - Data from the US Census Bureau and from the Centers for Disease Control 
    and Prevention, National Center for Health Statistics. National Vital 
    Statistics System, Natality on CDC WONDER Online Database.

- RSV data:
    - The National Respiratory and Enteric Virus Surveillance System (NREVSS)
    data at national and state level.
    - The [Weekly Rates of Laboratory-Confirmed RSV Hospitalizations from the RSV-NET Surveillance System](https://data.cdc.gov/Public-Health-Surveillance/Weekly-Rates-of-Laboratory-Confirmed-RSV-Hospitali/29hc-w46k)
    - The [National Emergency Department Visits for COVID-19, Influenza, and Respiratory Syncytial Virus](https://www.cdc.gov/ncird/surveillance/respiratory-illnesses/index.html)

For more information, please consult the associated 
[README file](./auxiliary-data/README.md).

## Data license and reuse

All source code that is specific to the overall project is available under an 
open-source [MIT license](https://opensource.org/licenses/MIT). We note that 
this license does NOT cover model code from the various teams, model scenario 
data (available under specified licenses as described above) and auxiliary data.

## Computational power

Those teams interested in accessing additional computational power should 
contact Katriona Shea at k-shea@psu.edu. Additional resources might be available from the [MIDAS Coordination Center](https://midasnetwork.us) - please contact questions@midasnetwork.us for information. 

## The RSV Scenario Modeling Hub Coordination Team    

 - Shaun Truelove, Johns Hopkins University
 - Cécile Viboud, NIH Fogarty
 - Justin Lessler, University of North Carolina
 - Sara Loo, Johns Hopkins University
 - Lucie Contamin, University of Pittsburgh
 - Emily Howerton, Penn State University
 - Claire Smith, Johns Hopkins University
 - Harry Hochheiser, University of Pittsburgh
 - Katriona Shea, Penn State University
 - Michael Runge, USGS
 - Erica Carcelen, John Hopkins University
 - Sung-mok Jung, University of North Carolina
 - Jessi Espino, University of Pittsburgh
 - John Levander, University of Pittsburgh
 - Katie Yan, Penn State University
