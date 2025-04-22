import pandas as pd
df=pd.read_csv('lesson-17/data/movie.csv')

def my_func(duration):
    if(duration<60):
        return "Short"
    elif 60<duration and duration<120:
        return "Medium"
    else:
        return "Long"
    

dff=df['duration'].apply(my_func)   
print(dff)