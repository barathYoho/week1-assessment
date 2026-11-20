import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../data/employees.csv')
print('Dataset loaded successfully')
display(df.head())

print('Dataset Shape:', df.shape)
df.info()
display(df.describe())

print('Average Salary:', df['salary'].mean())
print('Median Salary:', df['salary'].median())
print('Minimum Salary:', df['salary'].min())
print('Maximum Salary:', df['salary'].max())

department_summary = df.groupby('department').agg(headcount=('id','count'), average_salary=('salary','mean'), maximum_salary=('salary','max'))
display(department_summary)

chennai_employees = df[df['city'] == 'Chennai']
display(chennai_employees)
print('Chennai Employee Count:', len(chennai_employees))

%timeit df.groupby('department')['salary'].mean()
