# Hyderabad House Price Prediction

This is my Machine Learning project for predicting house prices in Hyderabad.

I worked on this project to understand how a real-world dataset can be used for data analysis, feature engineering, machine learning and finally converted into a simple web application using Streamlit.

## About the Project

The main aim of this project is to predict the approximate price of a property in Hyderabad based on some property details.

The user can enter:

- Location
- Area in square feet
- BHK
- Property Type
- Building Status

The trained Machine Learning model then predicts the approximate house price in lakhs.

## Dataset

I used a Hyderabad house price dataset containing around 3660 property records.

Some of the important columns in the dataset were:

- Location
- Price
- Area
- Rate per square feet
- Building Status
- Property Title

During the data analysis, I also extracted BHK and Property Type from the property title.

## Data Analysis

Before training the model, I performed different steps to understand the dataset.

Some of the things I checked were:

- Missing values
- Duplicate values
- Distribution of house prices
- Relationship between area and price
- Location-wise prices
- Building status and price
- BHK and price
- Property type and price
- Outliers
- Correlation between numerical features

I also checked for data leakage and removed `rate_persqft` from the final model because it is closely related to the target price.

## Machine Learning

I tried Linear Regression as a baseline model and then used Random Forest Regressor.

After tuning the Random Forest model, I got better results than the Linear Regression model.

The final model was trained using:

- Random Forest Regressor
- One Hot Encoding for categorical features
- Numerical features such as area and BHK
- Scikit-learn Pipeline

## Model Performance

The final pipeline gave approximately:

- MAE: 26.71 lakhs
- RMSE: 84.99 lakhs
- R² Score: 0.764

These results are from my test dataset.

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

## Streamlit Application

I also created a simple Streamlit web application for the trained model.

The application allows the user to enter property details and get a predicted house price.

## Project Structure

```text
Hyderabad-House-Price-Prediction/
│
├── app.py
├── house_price_prediction_hyd.ipynb
├── Hyderabad_House_price.csv
├── house_price_model.pkl
├── requirements.txt
└── README.md
