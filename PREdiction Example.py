from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import yfinance as yf
'''
Zipline is a Python library for backtesting trading strategies. It allows you to develop and test strategies using real-world data in a simulated environment.
The code we've been workixng on is not similar to Zipline in that it's not designed for backtesting trading strategies etc
Instead, it's a simple script to calculate financial metrics (ROI, ROEde, and CAGR) for a specific stock using data from Yahoo Finance.
If you're interested in backtesting trading strategies, you might want to consider using Zipline or a similar library. 
These libraries provide a lot of functionality for developing, testing, and optimizing trading strategies. However, they also require a good understanding of both programming and financial markets to use effectively.
'''
# Download historical market data
df = yf.download('AAPL', start='2020-01-01', end='2022-12-31')
#downloaded

# Calculate the percentage change
df['Return'] = df['Close'].pct_change()

# Drop missing values
df = df.dropna()

# Use the past 10 days' returns to predict the next day's return
df['Return1'] = df['Return'].shift(-1)
df['Return2'] = df['Return'].shift(-2)
df['Return3'] = df['Return'].shift(-3)
df['Return4'] = df['Return'].shift(-4)
df['Return5'] = df['Return'].shift(-5)
df['Return6'] = df['Return'].shift(-6)
df['Return7'] = df['Return'].shift(-7)
df['Return8'] = df['Return'].shift(-8)
df['Return9'] = df['Return'].shift(-9)
df['Return10'] = df['Return'].shift(-10)

# Drop missing values
df = df.dropna()

# Define features and target
features = df[['Return', 'Return1', 'Return2', 'Return3', 'Return4', 'Return5', 'Return6', 'Return7', 'Return8', 'Return9']]
target = df['Return10']

# Split the data into training and test sets
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(features_train, target_train)

# Make predictions
predictions = model.predict(features_test)

# Print the first 10 predictions
print(predictions[:10])

# Calculate metrics
mae = mean_absolute_error(target_test, predictions)
mse = mean_squared_error(target_test, predictions)
#r^2 metric
r2 = r2_score(target_test, predictions)

# Print metrics
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
