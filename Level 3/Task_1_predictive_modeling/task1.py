import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

from sklearn.model_selection import GridSearchCV
df = pd.read_csv("churn-bigml-20.csv")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
print("\nChurn Distribution:")
print(df["Churn"].value_counts())# Encode categorical variables

encoder = LabelEncoder()

df["State"] = encoder.fit_transform(df["State"])

df["International plan"] = encoder.fit_transform(df["International plan"])

df["Voice mail plan"] = encoder.fit_transform(df["Voice mail plan"])
df["Churn"] = df["Churn"].astype(int)
X = df.drop("Churn", axis=1)

y = df["Churn"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
print("Training set:", X_train.shape)
print("Testing set:", X_test.shape)
# Logistic Regression

log_model = LogisticRegression(random_state=42)

log_model.fit(X_train, y_train)

log_pred = log_model.predict(X_test)
# Decision Tree

tree_model = DecisionTreeClassifier(random_state=42)

tree_model.fit(X_train, y_train)

tree_pred = tree_model.predict(X_test)
# Random Forest

forest_model = RandomForestClassifier(random_state=42)

forest_model.fit(X_train, y_train)

forest_pred = forest_model.predict(X_test)
def evaluate_model(name, y_true, y_pred):

    print("\n" + "="*50)
    print(name)
    print("="*50)

    print("Accuracy :", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred))
    print("Recall   :", recall_score(y_true, y_pred))
    print("F1 Score :", f1_score(y_true, y_pred))

    print("\nClassification Report")

    print(classification_report(y_true, y_pred))
#
evaluate_model("Logistic Regression", y_test, log_pred)

evaluate_model("Decision Tree", y_test, tree_pred)

evaluate_model("Random Forest", y_test, forest_pred)
# Hyperparameter Tuning for Decision Tree

param_grid = {
    "criterion": ["gini", "entropy"],
    "max_depth": [3, 5, 10, None],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4]
}

grid_search = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("\nBest Parameters:")
print(grid_search.best_params_)

print("\nBest Cross Validation F1 Score:")
print(grid_search.best_score_)
best_tree = grid_search.best_estimator_

best_pred = best_tree.predict(X_test)

print("\n")
print("=" * 50)
print("Tuned Decision Tree")
print("=" * 50)

print("Accuracy :", accuracy_score(y_test, best_pred))
print("Precision:", precision_score(y_test, best_pred))
print("Recall   :", recall_score(y_test, best_pred))
print("F1 Score :", f1_score(y_test, best_pred))

print("\nClassification Report")
print(classification_report(y_test, best_pred))
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_estimator(best_tree, X_test, y_test)

plt.title("Confusion Matrix - Tuned Decision Tree")

plt.savefig("confusion_matrix.png")

plt.show()
import pandas as pd

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": best_tree.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

plt.figure(figsize=(10,6))

plt.barh(
    importance["Feature"],
    importance["Importance"]
)

plt.xlabel("Importance")
plt.title("Decision Tree Feature Importance")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig("feature_importance.png")

plt.show()