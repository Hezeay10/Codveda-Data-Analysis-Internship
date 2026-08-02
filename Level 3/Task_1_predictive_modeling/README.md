# Customer Churn Prediction using Machine Learning

## Project Overview

This project was completed as part of the Codveda Technologies Data Analytics Internship (Level 3 - Task 1).

The objective was to build and evaluate multiple classification models to predict whether a customer will churn.

---

## Dataset

Dataset: churn-bigml-20.csv

Target Variable:
- Churn

Features include:

- Account Length
- State
- International Plan
- Voice Mail Plan
- Call Statistics
- Charges
- Customer Service Calls

---

## Tools Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

---

## Project Workflow

- Data exploration
- Missing value check
- Label encoding of categorical variables
- Feature scaling using StandardScaler
- Train-test split
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Hyperparameter tuning using GridSearchCV
- Model evaluation
- Confusion matrix visualization
- Feature importance analysis

---

## Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 85.82% |
| Decision Tree | 92.54% |
| Random Forest | 92.54% |
| Tuned Decision Tree | 91.79% |

---

## Conclusion

Decision Tree produced the best balance between precision, recall, and F1-score for predicting customer churn. Hyperparameter tuning using GridSearchCV produced a robust model with comparable performance.