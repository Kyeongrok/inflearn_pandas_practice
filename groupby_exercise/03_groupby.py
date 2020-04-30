import pandas as pd
pd.set_option('max_columns', None)

df = pd.read_csv('score_figure.csv')
df['total'] = df['score1'] + df['score2'] + df['score3'] + df['score4'] + df['score5']
df['result'] = df['difficulty'] * df['total']

gr = df[['name', 'result', 'total']].groupby('name')
# print(gr.describe())

gr_agg = gr.agg(['sum', 'mean'])
# print(gr_agg)
gr_sorted = gr_agg['result'].sort_values('mean', ascending=False)

gr_sorted['mean'].to_excel('score_figure.xlsx')
