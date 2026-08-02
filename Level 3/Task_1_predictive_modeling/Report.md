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

Three machine learning models were developed to predict customer churn: Logistic Regression, Decision Tree, and Random Forest. Model performance was evaluated using Accuracy, Precision, Recall, and F1-score. The Decision Tree classifier produced the best balance between precision and recall, achieving an accuracy of approximately 92.5% with an F1-score of 0.69. Hyperparameter tuning was performed using GridSearchCV to optimize the Decision Tree model. Feature importance analysis showed that Total Day Minutes, Customer Service Calls, and Total Day Charge were the most influential predictors of customer churn. Overall, the Decision Tree model was selected as the most suitable classifier for this dataset.