import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

start_date = '2023-01-01'
end_date = '2024-01-01'

stock_data = yf.download('GOOGL', start=start_date, end=end_date)

stock_close_prices = stock_data['Close']

stock_close_prices.plot(kind='line', figsize=(10, 6))
plt.title('Historical Stock Prices of Alphabet Inc. (GOOGL)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.show()
