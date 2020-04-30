import pandas as pd

df = pd.read_csv('sales_years.csv')

gr = df.groupby('id')

gr_sum = gr.sum()
# print(gr_sum['amount'])

gr_mean = gr.mean()
# print(gr_mean['amount'])

gr_count = gr.count()
print(gr_count)
