import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
        'Student ID' : [1,2,3,4,5],
        'Student Name' : ['ALice','Bob','Charlie','Darrel','Enoch'],
        'Math Score' : [88,75,90,60,85],
        'Science Score' : [65,87,89,76,67],
        'English Score': [67,87,68,98,70]
        }
df=pd.DataFrame(data)
print(df)

print("------------------------------------------")

print(df[['Student Name','Science Score']],"\n")

print(df[['Student Name','Math Score']],"\n")

print(df[['Student Name','English Score']],"\n")

print("------------------------------------------")

"Selecting multiple row"
print(df[:3],"\n")

"Selecting Index of a Single Row"
print(df.loc[1],"\n")

"Selecting subset of row and column"

print(df.loc[1:3,['Student Name','Math Score']],"\n")

"Selecting Rows and Column using iloc"

print(df.iloc[0:3 , 2:4],"\n")

"Selecting Boolean Indexing  Students with Math Score > 80"

print(df[df['Math Score']>80],"\n")

"Conditional Selectiion with Multiple COnditions"
"""
print(df[(df['Math Score']>80)]) & [(df['Science Score']>75)],"\n")
"""

"Setting a Custom Index Using Stud Id"

df.set_index('Student ID',inplace = True)
print("DataFrame with custom index(Student ID):")

print(df, "\n")

"Resetting the index to the default"

df.reset_index(inplace = True)
print(df,"\n")