import pandas as pd

titanic_file=pd.read_excel('lesson-17/data/titanic.xlsx')
def classify_age(age):
    return "Child" if age<18 else "Adult"

titanic_file['Age_Group']=titanic_file['Age'].apply(classify_age)

print(titanic_file)