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

`malls2kmRadius.ipynb`

- Identifies the malls that are within a 1km radius from each HDB flat if the opening date of the mall is before the flat's transaction record date. Geometric distances between points are taken into account using `geopy`.

`distance2cbd.ipynb`

- Calculates the distance from HDB to Central Business District area (Coordinate(lon=103.851784, lat=1.287953)). Geometric distances between points are taken into account using `geopy`. 

`word_embedding.ipynb`

- Combine name and distance information about POIs (mrt, sch, mall)
- Convert to POI density vector using `spacy`

`pre_modelling.ipynb`



### Model Building

Working dataset: https://drive.google.com/drive/folders/1LEXFn1MAb0m7xJCqPMAyjJMXiA7_Ep6d?usp=drive_link

`xgboost_model.ipynb`

- Train xgboost regressor on working dataset
- Predict 2024 resale prices and evaluate performance


Geographically Neural Network Weighted Regression (GNNWR)




