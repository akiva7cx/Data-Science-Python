# -*- coding: utf-8 -*-
"""
DATA FRAME
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data={
      'Employee ID':[101,102,103,104,105,106],
      'Name':['Allen','Balboa','Chinna','Eleven','Joshua','Azaguraja'],
      'Age':[29,30,28,24,np.nan,41],
      'Department':['HR','IT','Finance','IT','HR','Finance'],
      'Salary':[50000,70000,80000,60000,55000,np.nan],
      'Performance_Rating':[4,5,3,4,5,5]
      }

df= pd.DataFrame(data)
print(df.isnull().sum())

print(df.head())

print(df.describe())


"""
df['Age']= df['Age'].fillna(df['Age'].mean())

df['Salary']= df['Salary'].fillna(df['Salary'].median())

print(df)
print(df.isnull().sum())

df.rename(columns={'Performance_Rating':'Rating'} , inplace = True)
print(df)


print(df.head())

print(df.describe())


sns.set(style='whitegrid')
plt.figure(figsize=(12,6))

sns.barplot()
"""


sns.set(style='white')
plt.figure(figsize=(12,6))
sns.barplot(data=df,x='Department',y='Salary',errorbar=None,palette='Blues_d')
plt.title('Average Salary by Departement')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.show()

print("------------")
print('scatterplot')
plt.figure(figsize=(12,6))
sns.scatterplot(data=df,x='Department',y='Salary',hue='Department',style = 'Department')


















