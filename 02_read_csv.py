# Pandas
import pandas as pd
df = pd.read_csv('asset.csv')

print(df.shape) # row, column(행, 열)

# row 행개수
print(df.shape[0])

# column 열개수
print(df.shape[1])
