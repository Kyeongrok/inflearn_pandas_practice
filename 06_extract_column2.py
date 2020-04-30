import pandas as pd

df = pd.read_json('election21_seoul.json')
# print(df)
df_re_arr = df[['선거구_시도명', '투표수', '더불어민주당', '미래통합당']]
print(df_re_arr)

df_re_arr.to_excel('election21_seoul.xlsx')
