import pandas as pd

titanic_file=pd.read_excel('lesson-17/data/titanic.xlsx')

summary=titanic_file.groupby(['Pclass']).agg({
    'Age':'mean',
    'Fare':'sum',
    'PassengerId':'count'
}).rename(columns={
    'Age': 'Average_Age',
    'Fare': 'Total_Fare',
    'PassengerId': 'Passenger_Count'
})

summary=summary.reset_index()
print(summary)