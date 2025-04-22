import pandas as pd

df=pd.read_csv('lesson-17/data/movie.csv')

df1 = df[['director_name', 'color']]
df2 = df[['director_name', 'num_critic_for_reviews']]

joined_1=pd.merge(df1,df2,on='director_name',how='left')

joined_2=pd.merge(df1,df2,on='director_name',how='outer')

# print(joined_2)

joined_1rows=len(joined_1)

joined_2rows=len(joined_2)

print(joined_1rows)
print(joined_2rows)