# Housing-Price-Time-Series-Forecasting

### Introduction

We aim to develop a time series forecasting model for predicting housing prices in Singapore's HDB
market using transaction data and geographical information.

### Data Cleaning & Processing

`mrt_coordinates_opening_dates.ipynb`

This file scrapes the MRT stations in Singapore through the Wikipedia website as well as their respective coordinates and opening dates. The results are written to the `mrt_stations.csv` file

`mall_coordinates_opening.ipynb`

This file scrapes the shopping malls in Singapore via Wikipedia and obtaining their respective coordinates and opening dates. 

`data_cleaning.ipynb`

This file deals with the following:
- Cleaning the HDB resale flat prices dataset 
    -  Converting `remaining_lease` into float for standardisation purposes and creating an `address` column that concatenates `block` and `street_name`.
    - Merging the two HDB resale flat prices datasets into one.
    - Calculating the coordinates of each unique HDB flat in the merged dataset using OneMapSG API.
-  Cleaning the `mrt_stations.csv` file
    - Remove rows where the MRT stations are yet to be opened (e.g. Brickland MRT Station).
    - Ensure that the opening dates are standardised,
- Cleaning the BTO supply dataset
    - Dropping redundant rows and remove rows with empty values.
    - Standardise the dates to `DD-MMM-YY`.
    - Add the coordinates of each BTO.
- Cleaning the SORA dataset
    - Creating new column `SORA Value Month` that will match the HDB transaction record dates.
    - Aggregating compounded SORA based on the month.

### Feature Engineering

`add_sora.ipynb`

Adds the SORA values associated with the HDB transaction record dates.

`mrt_stations_nearby_and_BTO_supply.ipynb`

- Identifies the MRT stations that are within a 1km radius from each HDB flat if the opening date of the MRT station is before the flat's transaction record date. For HDB flats that do not have any MRT stations within a 1km radius, the nearest MRT station is noted. Geometric distances between points are taken into account using `GeoPandas`.
- Identifies the number of BTO flats that are launching within a 4km radius from the flat (the launch dates of the BTOs are compared with the flat's transaction record date - only launch dates that happen before the transaction record date are taken into account) and the supply of units associated with these BTOs.

### Model Building

Geographically Neural Network Weighted Regression (GNNWR)






## Tasks (To remove once finalised)


### Feature Engineering


#### Retrieving travelling distance with Google Maps API
API Doc: https://developers.google.com/maps/documentation/distance-matrix/start
Pricing: https://developers.google.com/maps/documentation/distance-matrix/usage-and-billing

For example, Distance to CBD attribute will cost $1,000 for 200,000 rows of data. 

Credit of $200-$300 for new users.






#### Data Cleaning 
- block + street (Done)
- mrt dataset (name + coordinates + opening) (Anders) ✅
- shopping mall dataset (name + coordinates + opening) (Joseph)


#### EDA (DO later)


#### Feature Engineering

Decision Points
- Word embedding will be used for POI reviews (we're not doing it for housing)
- Rationale for not using address script data - not feasible

Attributes
- Distance2CBD (float) -- steps: openrouteservice API (Joseph)
- Number of MRT Stations within 1km (int) -- steps: openrouteservice API and counter (Anders)

- Reviews of POI of Shopping Mall + Schools (word embedding will be used here) 
    - All schools within 2km -- steps: openrouteservice API
    - All shopping malls within 2km -- steps: openrouteservice API 
        - Should we use supermarkets (1km) [KIV]

    Figure out how to get the reviews

    Steps
    1. Gather schools + shopping malls data
    2. Use ChatGPT to get information about school + shopping mall
    3. Apply word embedding

- Number of BTO within 4km of that address in that period of time (Anders)

- SORA rates (Joseph)

- Number of Clinics within 5km radius [KIV]



- investigate deep learning (Anders)
- investigate word embedding + graph modelling (Joseph)