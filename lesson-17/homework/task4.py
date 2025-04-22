import pandas as pd

movie_file=pd.read_csv('lesson-17/data/movie.csv')

df1=movie_file.groupby(['color','director_name'])

result=df1.agg({
    'num_critic_for_reviews':'sum',
    'duration':'mean'
})
print(result)