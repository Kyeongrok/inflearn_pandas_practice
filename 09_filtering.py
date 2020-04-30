import pandas as pd

df = pd.read_csv('asset2.csv')

# age >= 30
df_filtered = df[df['age'] >= 30]

# age >= 30, location == '종로구'
df_mul_case = df[ (df['age'] >= 30) & (df['location'] == '종로구') & (df['age'] < 34) ]
print(df_mul_case)
