import pandas as pd

df = pd.read_csv('asset.csv')
# print(df)
df_sorted = df.sort_values(['age']) # ascending

df_sort_desc = df.sort_values(['age'], ascending=False)
# print(df_sort_desc)

# 나이 내림차순 나이가 같을 때 두번째 조건은 이름을 오름차순
df_sort_mul_case = df.sort_values(['age', 'name'], ascending=[False, True])
# daniel, mimi
print(df_sort_mul_case)

