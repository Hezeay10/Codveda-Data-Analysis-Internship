# Import libraries

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset

df = pd.read_csv("Stock Prices Data Set.csv")

# Select required columns and remove missing values

df = df[['open', 'close']].dropna()

# Features and target

X = df[['open']]
y = df['close']

# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model

model = LinearRegression()
model.fit(X_train, y_train)

# Predictions

y_pred = model.predict(X_test)

# Evaluation

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("Model Evaluation")
print("-------------------------")
print(f"Mean Absolute Error: {mae:.4f}")
print(f"Mean Squared Error: {mse:.4f}")
print(f"Root Mean Squared Error: {rmse:.4f}")
print(f"R² Score: {r2:.4f}")

# Visualization

plt.figure(figsize=(8,5))

plt.scatter(y_test, y_pred, alpha=0.4, s=10)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color='red',
    linewidth=2,
    label="Perfect Prediction"
)

plt.xlabel("Actual Closing Price")
plt.ylabel("Predicted Closing Price")
plt.title("Actual vs Predicted Stock Closing Prices")
plt.legend()

plt.savefig("actual_vs_predicted.png",
            dpi=300,
            bbox_inches="tight")

plt.show()