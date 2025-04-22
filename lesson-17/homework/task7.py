import pandas as pd
df=pd.read_csv('lesson-17/data/employee.csv')

def normalize(group):
    min_salary=group['BASE_SALARY'].min()
    max_salary=group['BASE_SALARY'].max()
    group['Normalized_salary']=group['BASE_SALARY']-min_salary/(max_salary-min_salary)
    return group

normalized=df.groupby(['DEPARTMENT']).apply(normalize)
print(normalized)
# print(df.columns)