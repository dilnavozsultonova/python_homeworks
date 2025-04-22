import pandas as pd

df1=pd.read_parquet('lesson-17/data/flights')

grouped=df1.groupby('Year','month')

df2=grouped.agg({
    'flights':'sum',
    'ArrDelay':'mean',
    'DepDelay':'max'
})

print(df2)