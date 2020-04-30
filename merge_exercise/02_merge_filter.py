import pandas as pd

df_kare = pd.read_csv('KARE.csv')
df_height = pd.read_csv('8842height.phe.csv')
df_kare = df_kare.rename(columns={'HumanID':'HID'})


df_merged = pd.merge(df_kare, df_height, on='HID')
# print(df_merged.count())

df_merged = df_merged[['Id', 'HID', 'Area', 'Age', 'Sex', 'Height_x']]
df_filtered = df_merged[(df_merged['Height_x'] >= 165) & (df_merged['Age'] >= 50)]
df_sorted = df_filtered.sort_values(['Age', 'Height_x'], ascending=[True, True])
print(df_sorted)

