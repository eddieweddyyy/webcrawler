import statsmodels.api as sm
import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\CKIRUser\Desktop\coding_eddie\Regression Analysis\california_housing.csv')
x = np.column_stack([df['age']**2, df['age']])
y = df['income']
model = sm.OLS(y, x).fit()
print(model.summary())