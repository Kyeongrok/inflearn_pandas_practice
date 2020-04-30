import pandas as pd

df = pd.read_csv('asset.csv')
# df['age']
# print(df)
age_asset = df[['age', 'asset']]
# print(age_asset)
re_arrange = df[['age','name','asset']]
print(re_arrange)
