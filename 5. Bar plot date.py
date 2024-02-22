import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

start_date = '2023-01-01'
end_date = '2024-01-01'

stock_data = yf.download('GOOGL', start=start_date, end=end_date)

stock_volume = stock_data['Volume']

stock_volume.plot(kind='bar', figsize=(10, 6), color='blue')
plt.title('Trading Volume of Alphabet Inc. (GOOGL)')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid(True)
plt.show()
