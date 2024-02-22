import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the time period
start_date = '2023-01-01'
end_date = '2024-01-01'

# Fetch historical stock data using Yahoo Finance API
stock_data = yf.download('GOOGL', start=start_date, end=end_date)

# Extract relevant data
stock_volume = stock_data['Volume']
stock_close_prices = stock_data['Close']

# Plotting the data
plt.figure(figsize=(10, 6))
plt.scatter(stock_close_prices, stock_volume, color='blue', alpha=0.5)
plt.title('Trading Volume vs Stock Prices of Alphabet Inc. (GOOGL)')
plt.xlabel('Stock Prices')
plt.ylabel('Trading Volume')
plt.grid(True)
plt.show()
