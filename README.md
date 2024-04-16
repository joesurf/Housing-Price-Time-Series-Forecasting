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


### Geographically Neural Network Weighted Regression (GNNWR)

### Long Short Term Memory

#### Data Preprocessing and Splitting

We first prepare the data for model training by performing necessary preprocessing steps and splitting it into distinct sets for training, validation, and testing purposes. The process involves:

1. Normalization of Numerical Features: Numerical features in the dataset are normalized to ensure uniform scaling, enhancing model convergence and performance.

2. Splitting the Dataset: The dataset is divided into three subsets:
   - Training Set: Used to train the model.
   - Validation Set: Employed to fine-tune model parameters and prevent overfitting.
   - Test Set: Reserved for final evaluation of model performance.
3. Conversion to Numpy Arrays: The data is converted into numpy arrays to facilitate efficient model training and compatibility with various machine learning frameworks.
4. Data Confirmation: Finally, the section concludes by printing the data types and shapes of the training and validation sets, providing a comprehensive overview of the prepared data for further processing.

#### LSTM Model Training

This section delves into the training and evaluation of a Long Short-Term Memory (LSTM) neural network model designed for predictive tasks. The process involves the following steps:

1. Model Construction: The LSTM model is built with three layers, each followed by dropout regularization to mitigate overfitting. This architecture enables the model to capture temporal dependencies effectively.
2. Compilation: The model is compiled using the Adam optimizer and mean squared error loss function, suitable for regression tasks.
3. Early Stopping: To prevent overfitting, early stopping is implemented with a patience of 5, monitoring validation loss during training. This mechanism halts training when the model's performance on the validation set starts deteriorating.
4. Training Process: The model is trained by fitting it to the training data for 100 epochs, utilizing a batch size of 32. Throughout the training process, model performance is evaluated on the validation set to assess its generalization capabilities and prevent overfitting.