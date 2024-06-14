import pandas as pd

df = pd.read_csv(r'C:\Users\CKIRUser\Desktop\coding_eddie\credit.csv')
# print(df)

# df = dataframe

# print(df['age'].mean())
# print(df['age'].mode())
# print(df['age'].max())
# print(df['age'].min())
# print(df['age'].describe())
new_df = df.groupby('gender')[['expenditure','frequency']].mean()

print(new_df)
