import pandas as pd

df = pd.read_json('water.json')
# print(df)

# 저렴 top 5 ---> 오름차순
df_sorted = df.sort_values(['price'])
# print(df_sorted.head(10))

# 비싼 top 10 ---> 내림차순
df_sorted_desc = df.sort_values(['price'], ascending=False)
# print(df_sorted_desc.head(10))
print(df['price'].mean())

# 비싼 99000, 싼 850 평균 13,334


