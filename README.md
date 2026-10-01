# Hyderabad House Price Prediction

A Machine Learning project for predicting house prices in Hyderabad based on property details such as location, area, BHK, property type and building status.

The project covers the complete Machine Learning workflow, starting from data analysis and feature engineering to model training, evaluation and deployment using Streamlit.

## About the Project

House prices can vary depending on factors such as location, property size, number of bedrooms, property type and building status.

The main aim of this project is to build a Machine Learning model that can estimate the approximate price of a Hyderabad property based on these details.

The Streamlit application allows users to enter:

- Location
- Area in square feet
- BHK
- Property Type
- Building Status

The trained model then predicts the approximate property price in lakhs.

## Dataset

The project uses a Hyderabad house price dataset containing around 3660 property records.

Some of the important columns include:

- Location
- Price
- Area in square feet
- Rate per square feet
- Building Status
- Property Title

The property title was further processed to extract useful features such as BHK and Property Type.

## Data Analysis

The dataset was explored to understand the relationship between different property features and house prices.

The analysis included:

- Checking missing values
- Checking duplicate records
- Understanding numerical features
- Price distribution
- Relationship between area and price
- Location-wise price analysis
- Building status and price analysis
- BHK-wise price analysis
- Property type analysis
- Outlier analysis
- Correlation analysis

A data leakage check was also performed. The `rate_persqft` feature was excluded from the final model because it is mathematically derived from the property price and area.

## Feature Engineering

The following features were prepared for the Machine Learning model:

- Location
- Area in square feet
- BHK
- Property Type
- Building Status

BHK and Property Type were extracted from the original property title.

Rare locations were grouped into an `Other` category to reduce the number of location categories.

Categorical features were converted into numerical features using One Hot Encoding.

## Machine Learning

Two regression models were evaluated during the project.

### Linear Regression

Linear Regression was used as the baseline model.

### Random Forest Regressor

Random Forest Regressor was then used to capture non-linear relationships between property features and price.

Hyperparameter tuning was performed using `RandomizedSearchCV`.

The tuned Random Forest model produced better test-set results than the Linear Regression baseline.

## Final Model

The final prediction workflow uses a Scikit-learn Pipeline containing:

- ColumnTransformer
- One Hot Encoder
- Random Forest Regressor

The trained pipeline was saved as `house_price_model.pkl` and is used by the Streamlit application for making predictions.

The model file is stored using Git LFS because of its size.

## Model Performance

The final pipeline produced the following results on the test dataset:

| Metric | Score |
|---|---:|
| MAE | 26.71 lakhs |
| RMSE | 84.99 lakhs |
| R² Score | 0.764 |

These results are based on the test data used during the project.

## Streamlit Application

A Streamlit web application was created to provide a simple interface for the trained Machine Learning model.

Users can enter property details and get an estimated house price.

### Application Screenshots

The screenshots of the application are available in the repository.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Random Forest
- Streamlit
- Jupyter Notebook
- Git
- Git LFS

## Project Structure

```text
Hyderabad-House-Price-Prediction/
│
├── app.py
├── house_price_prediction_hyd.ipynb
├── house_price_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
├── .gitattributes
└── application screenshots
