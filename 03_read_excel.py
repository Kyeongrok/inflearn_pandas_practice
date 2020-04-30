# df
import pandas as pd

df = pd.read_excel('sales.xlsx', sheet_name='month2')
print('--->')
print(df['amount'].sum())
print(df['amount'].mean())
