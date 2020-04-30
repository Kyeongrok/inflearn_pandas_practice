import pandas as pd

df_employee = pd.read_csv('employee_list.csv')
df_amt_p_year = pd.read_csv('amount_per_year.csv')

# join --> database
df_merged = pd.merge(df_employee, df_amt_p_year, on='id')
# print(df_merged)
df_merged.to_excel('merged.xlsx')

# 2020년도에 연봉 대비 물건(자동차)을 얼마나 팔았다
# 2020년 필터링
df2020 = df_merged[df_merged['year'] == 2021]
df_sorted = df2020.sort_values(['amount'], ascending=False)
# print(df_sorted)

# 연봉 대비 많이 판 사람은?
# salary / amount = 한대 파는데 얼마의 salary가 들었나
df_sorted['output'] = df_sorted['salary'] / df_sorted['amount']
df_sorted = df_sorted.sort_values(['output'])
print(df_sorted.head(5))
