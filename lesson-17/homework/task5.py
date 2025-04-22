import pandas as pd

df1=pd.read_parquet('lesson-17/data/flights')

grouped=df1.groupby('Year','Quarter','Month')

df2=grouped.agg({
    'flights':'sum',
    'ArrDelay':'mean',
    'DepDelay':'max'
})
print(df2)
# print(df1.columns)