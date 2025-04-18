import pandas as pd
import numpy as np


json_file=pd.read_json("lesson-16/homework/data/iris.json")
new_columns = [column.lower() for column in json_file.columns]

json_file.columns=new_columns
print(json_file[["sepallength", "sepalwidth"]])

exe_file=pd.read_excel("lesson-16/homework/data/titanic.xlsx")
exe_file["filtered_rows"] = np.where(exe_file["Age"] <30,"young","old")
gender = exe_file["Sex"]

from collections import Counter

nums = Counter(gender)
print(nums)

par_file=pd.read_parquet("lesson-16/homework/data/flights")

col = par_file.columns

par_file=par_file[["Origin","Dest","Carrier"]]
print(par_file)

print(len(set(par_file["Dest"])))

csv_file=pd.read_csv("lesson-16/homework/data/movie.csv")
csv_file = csv_file[csv_file["duration"] > 120]
csv_file.sort_values(by="director_facebook_likes", ascending=False)
print(csv_file.head(5))

