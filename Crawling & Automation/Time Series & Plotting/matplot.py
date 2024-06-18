import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data


df = data.DataReader('005930', 'naver', start='2023-06-17', end='2024-06-17')
plt.plot(df.index, df['Close'], color="crimson")
plt.xlabel('time')
plt.ylabel('price')
plt.legend(['Samsung Electronics'])
plt.title('Stock')
plt.show()

plt.bar([1,2,3], [10,20,30])
plt.show()

plt.pie([57,35,11], labels=['ramen', 'tuna', 'snack'])
plt.show()

plt.hist([160,165,170,171,172,180])
plt.show()

math = [5, 8, 23, 5, 67, 34, 34, 23]
english = [23, 6, 3, 1, 5, 45, 54, 34]
plt.scatter(math, english)
plt.show()

plt.stackplot([1,2,3], [10,20,30], [30,20,50])
plt.show()

plt.figure(figsize=(10,10))
plt.plot([1,2,3],[10,20,30])
plt.plot([1,2,3],[30,60,90])
plt.show()

import yfinance as yfin

yfin.pdr_override()
df = data.get_data_yahoo('AMZN', start='2023-01-01', end='2024-01-01')
df20 = df['Close'].rolling(20).mean()
df60 = df['Close'].rolling(60).mean()
plt.plot(df.index, df20)
plt.plot(df.index, df60)
plt.show()

time = [2018, 2019, 2020, 2021]
samsung = [50000, 60000, 75000, 70000]
lg = [30000, 40000, 50000, 35000]

plt.plot(time, samsung, color="purple")
plt.plot(time, lg)
plt.xlabel('time')
plt.ylabel('sales')
plt.legend(['Samsung', 'LG'])

plt.show()

import yfinance as yfin
yfin.pdr_override()
df = data.get_data_yahoo('BTC-USD', start='2023-01-01', end='2024-01-01')
avg = df['Volume'].mean()
df['HigherVolume'] = df['Volume'] > avg
# print(df)
a = df[df['HigherVolume']==True]
# print(a)

plt.bar(a.index, a['Close'])
plt.show()