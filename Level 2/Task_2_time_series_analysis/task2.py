import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose
df = pd.read_csv("Stock Prices Data Set.csv")
print(df.head())

print(df.info())
# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])
# Sort by date
df = df.sort_values("date")
# Select Apple stock
apple = df[df["symbol"] == "AAPL"].copy()
apple.set_index("date", inplace=True)
print(apple.head())
print(apple.shape)
plt.figure(figsize=(12,6))

plt.plot(apple.index, apple["close"], label="Closing Price")

plt.title("Apple Stock Closing Price Over Time")

plt.xlabel("Date")
plt.ylabel("Closing Price")

plt.legend()

plt.grid(True)

plt.savefig("time_series_plot.png", dpi=300, bbox_inches="tight")

plt.show()
# Time Series Decomposition

decomposition = seasonal_decompose(
    apple["close"],
    model="additive",
    period=252
)

fig = decomposition.plot()

fig.set_size_inches(12, 8)

plt.savefig(
    "time_series_decomposition.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
# 30-Day Moving Average

apple["Moving Average"] = apple["close"].rolling(window=30).mean()

plt.figure(figsize=(12,6))

plt.plot(
    apple.index,
    apple["close"],
    label="Closing Price",
    alpha=0.6
)

plt.plot(
    apple.index,
    apple["Moving Average"],
    label="30-Day Moving Average",
    linewidth=2
)

plt.title("Apple Stock Price with 30-Day Moving Average")

plt.xlabel("Date")
plt.ylabel("Closing Price")

plt.legend()
plt.grid(True)

plt.savefig(
    "moving_average.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()