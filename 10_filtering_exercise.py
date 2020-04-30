import pandas as pd

df = pd.read_json('water.json')

# 1020,493 price >= 100000, price <= 20000
df_filtered = df[(df['price'] >= 10000) & (df['price'] <= 20000)]
df_sorted = df_filtered.sort_values(['price'])
print(df_sorted)
