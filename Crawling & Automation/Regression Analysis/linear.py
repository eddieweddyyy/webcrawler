import numpy as np
height = np.array([170,180,160,165,158,176,182,172]).reshape(-1,1)
weight = np.array([75,81,59,70,55,78,84,72]).reshape(-1,1)

import matplotlib.pyplot as plt
plt.scatter(height,weight)
plt.show() 
#-----------------------------------------------------------------------

from sklearn.linear_model import LinearRegression

model = LinearRegression().fit(height, weight)
print(model.score(height, weight)) #R value
print(model.intercept_)
print(model.coef_)

a = model.predict([[170], [180]])
print(a)
#-----------------------------------------------------------------------

plt.scatter(height, weight)
plt.plot(height, model.predict(height), color="purple")
plt.show()

import statsmodels.api as sm
model = sm.OLS(weight, height).fit()
print(model.summary())
#-----------------------------------------------------------------------

import pandas as pd
df = pd.read_csv(r'C:\Users\CKIRUser\Desktop\coding_eddie\Regression Analysis\california_housing.csv')

model = sm.OLS(df['price'], df[['year', 'rooms', 'bedrooms']]).fit()
print(model.summary())

a = model.predict([20, 1000, 200], [], [])
print(a)
#-----------------------------------------------------------------------
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_table('income.txt')
df = df.dropna()

def temp(x, a, b, c):
  return a*x**2 + b*x + c

opt, cov = curve_fit(temp, df['age'], df['income'])
print(opt)
a,b,c = opt

import numpy as np

x = np.array(df['age'])
x = np.array([1,2,3,4,5,6])
plt.scatter(df['age'], df['income'])

plt.plot(x, temp(x, a, b, c))
plt.show()