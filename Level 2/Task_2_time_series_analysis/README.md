# Time Series Analysis of Apple Stock Prices

## Project Overview

This project was completed as part of the Codveda Technologies Data Analytics Internship (Level 2 - Task 2).

The objective was to analyze historical Apple stock prices to identify trends, decompose the time series into its components, and apply moving average smoothing.

---

## Dataset

Stock Prices Data Set.csv

Selected Stock:
- Apple (AAPL)

Columns Used:
- Date
- Close Price

---

## Tools Used

- Python
- Pandas
- Matplotlib
- Statsmodels

---

## Project Steps

- Loaded the dataset
- Converted the date column into datetime format
- Sorted data chronologically
- Selected Apple stock records
- Set the date as the index
- Plotted the stock closing prices
- Performed seasonal decomposition
- Applied a 30-day moving average
- Saved all generated visualizations

---

## Visualizations

### Time Series Plot
Shows the daily closing prices of Apple stock over time.

### Time Series Decomposition
Separates the time series into:
- Trend
- Seasonal
- Residual components

### Moving Average
Displays the original closing prices alongside the 30-day moving average to smooth short-term fluctuations.

---

## Conclusion

The time series analysis reveals long-term price trends and short-term fluctuations in Apple's stock prices. Seasonal decomposition helps isolate the trend, seasonal, and residual components, while the moving average provides a clearer view of the underlying trend by reducing daily noise.