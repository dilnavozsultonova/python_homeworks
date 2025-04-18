import numpy as np
import pandas as pd

iris = pd.read_json("lesson-16/homework/data/iris.json")
print(iris.describe())

titanic = pd.read_excel("lesson-16/homework/data/titanic.xlsx")
print(titanic["Age"].min())
print(titanic["Age"].max())
print(titanic["Age"].sum())

movie = pd.read_csv("lesson-16/homework/data/movie.csv")
print(movie[movie["director_facebook_likes"] == movie["director_facebook_likes"].max()])
top5 = movie.fillna(0).sort_values(by="duration", ascending=False).head(5)
print(top5)

flight = pd.read_parquet("lesson-16/homework/data/flights")
flight.select_dtypes("number").fillna(0,inplace=True)
print(flight)