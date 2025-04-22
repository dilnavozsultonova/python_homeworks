import pandas as pd

titanic_file = pd.read_excel('lesson-17/data/titanic.xlsx')


titanic_pipeline = (
    titanic_file[titanic_file['Survived'] == 1]  
    .copy()
)


mean_age = titanic_pipeline['Age'].mean()
titanic_pipeline['Age'].fillna(mean_age, inplace=True)


titanic_pipeline['Fare_Per_Age'] = titanic_pipeline['Fare'] / titanic_pipeline['Age']

print(titanic_pipeline[['Name', 'Survived', 'Age', 'Fare', 'Fare_Per_Age']].head())
