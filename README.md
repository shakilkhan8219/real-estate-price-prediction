## ImmoEliza_House_Prediction
### Description

This project describe the prices prediction of property (houses) according to current prices on the Belgium market .

* The Belgian famous site for sell & buy houses, IMMOWEB, is used to collect data about current prices of properties in Belgium .

* The Main project is divided into three sub-parts.
    - Data acquisition.
    - Data cleaning and preprocessing .
    - Machine learning.
    - Test & deployment.

## Data acquisition:

In this Part of the project data related to prices and all other information related to properties were collected by scraping the immoweb. 
beautifulsoup were used for extracting Links of the properties.
All the required information related to property 
from all the links were saved in a file(.CSV).

## Data cleaning and preprocessing

In this part data cleaning and preprocessing were performed in order to make data ready for analysis. 

steps performed:

- Droping all the unwanted features and rows. 
- Sorting missing values.
- Missing values in numerical data was imputed either by medien.
- important features in data were selected by using Feature selection method.  
 
Analysis was performed by generating different plots.

- Plot fot price comperison in different provinces in Belgium

## Machine learning:

In this project Linear Regression model is used to estimate the price for houses in Belgium
with the given features.

### Objective:
Apply a linear regression on  preprocess data for Machine Learning

### Working Process:

Data was organised for Machine learning step.
Prior to dividing final data into traning and test set, numerical values were normalised.
Then linear regression model were used for model traning and price predection.

## Data acquisition.
In this Part of the project data related to 
prices and all other information related to 
properties were collected by scraping the immoweb. 
beautifulsoup were used for extracting Links of the properties.
All the required information related to property 
from all the links were saved in a file(.CSV).
