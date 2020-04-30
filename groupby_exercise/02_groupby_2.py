import pandas as pd
pd.set_option('max_columns', None)

df = pd.read_csv('sales_years.csv')
gr = df.groupby('id')

# print(gr.describe())

print(gr.agg(
    {'amount':['count', 'sum', 'mean', 'std'],
     'year':['count']}
))