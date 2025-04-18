import sqlite3
import numpy as np
import pandas as pd

with sqlite3.connect('lesson-16/homework/data/chinook.db') as connection:
    df_employee = pd.read_sql(
        "SELECT * FROM customers",
        con=connection
    )
print(df_employee.head(10))

js=pd.read_json("lesson-16/homework/data/iris.json")
print(js.shape)
print(js.columns)

exe2=pd.read_excel("lesson-16/homework/data/titanic.xlsx")
print(exe2.head(5))

pr=pd.read_parquet("lesson-16/homework/data/flights")
print(pr.info())

csv_file=pd.read_csv("lesson-16/homework/data/movie.csv")
print(csv_file.sample(10))
