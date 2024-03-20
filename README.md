# Housing-Price-Time-Series-Forecasting


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