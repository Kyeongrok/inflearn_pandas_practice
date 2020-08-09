import pandas as pd

df = pd.read_csv('score.csv')

print(df)
print(df['math'])

df['total'] = df.apply(lambda x: x['math'] + x['english'] + x['physical_education'], axis=1)

print(df)