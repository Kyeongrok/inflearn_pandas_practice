import pandas as pd
import openpyxl
df = pd.read_json('sales.json')
# df['total'] = 0
df['total'] = df['price'] * df['amount']
print(df)

df.to_excel('sales_total.xlsx')