# Stock Price Regression Analysis

## Project Overview

This project was completed as part of the Codveda Technologies Data Analytics Internship (Level 2 - Task 1).

The objective is to build a Linear Regression model that predicts stock closing prices using stock opening prices.

---

## Dataset

Stock Prices Data Set.csv

Features:

- Symbol
- Date
- Open Price
- High Price
- Low Price
- Close Price
- Volume

---

## Tools Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

---

## Steps Performed

- Loaded the dataset
- Removed missing values
- Selected Open Price as the independent variable
- Selected Close Price as the dependent variable
- Split the dataset into training and testing sets
- Built a Linear Regression model
- Evaluated model performance
- Visualized Actual vs Predicted values

---

## Model Evaluation

| Metric | Result |
|---------|---------|
| MAE | 0.7692 |
| MSE | 2.7261 |
| RMSE | 1.6511 |
| R² Score | 0.9997 |

---

## Visualization

The scatter plot compares the actual closing prices against the predicted closing prices. A red reference line represents perfect predictions, showing that the model predictions closely follow the actual values.

---

## Conclusion

The Linear Regression model achieved excellent performance with an R² score of approximately 0.9997, indicating that the opening price is a strong predictor of the closing price.