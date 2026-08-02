# Predictive Modeling Report

## Objective

Build and evaluate multiple classification models to predict customer churn.

## Dataset

Customer Churn Dataset

667 observations

Target:
- Churn

## Preprocessing

- Label Encoding
- Feature Scaling
- Train-Test Split

## Models

- Logistic Regression
- Decision Tree
- Random Forest

## Hyperparameter Tuning

GridSearchCV was used to optimize the Decision Tree classifier.

Best Parameters:

- criterion = gini
- max_depth = 10
- min_samples_leaf = 1
- min_samples_split = 5

## Evaluation Metrics

Accuracy

Precision

Recall

F1-score

## Visualizations

- Confusion Matrix
- Feature Importance

## Conclusion

The Decision Tree model achieved the best overall balance for customer churn prediction and was selected as the preferred classifier.