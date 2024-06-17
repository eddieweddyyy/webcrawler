import pandas as pd
from pandas_datareader import data
import yfinance as yfin

yfin.pdr_override()
df = data.get_data_yahoo('AAPL', start='2024-01-01', end='2024-06-17')
print(df['Close'].plot())

df2 = data.DataReader('005930', 'naver', start='2024-01-01', end='2024-06-17')
print(df2.index)
df2['Close'] = df2['Close'].astype(float)
print(df2['Close'].plot())
# print(df2)

# print(df)

df2['rolling5'] = df2['Close'].rolling(5).mean()
df2['rolling5'].plot()
new = df2['Close'].rolling(20).mean()
new = df2['Close'].rolling(5).sum()

print(df2)