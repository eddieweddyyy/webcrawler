import pandas as pd

df = pd.read_csv(r'C:\Users\CKIRUser\Desktop\coding_eddie\credit.csv')
# print(df)

# df = dataframe

# print(df['age'].mean())
# print(df['age'].mode())
# print(df['age'].max())
# print(df['age'].min())
# print(df['age'].describe())
new = df.groupby('gender')[['expenditure','frequency']].mean()


new = df[['age', 'expenditure']].corr()

new = df[ df['age'] > 50 ]
new = df.query("age > 50 and marriage == 'Married'")

shirts = [15, 20, 25]
pants = [150, 160, 170]

dic = {
    'shirts' : [15, 25, 25],
    'pants' : pants
}

df2 = pd.DataFrame(dic)


new1 = df.query("gender == 'M' and marriage == 'Married'")[['age', 'expenditure', 'frequency']].mean()
new2 = df.query("gender == 'M' and marriage == 'Single'")[['age', 'expenditure', 'frequency']].mean()

new3 = df.groupby('income')[['age', 'expenditure', 'frequency']].mean()

