"""SERIES IN PANDAS
"""

import pandas as pd  #
data = pd.Series([4,5,6,7])
print(data)

print(data.values)
print(data.index)

print(data[1])
print(data[0:3])

data0 ={
         'Chennai':5000,
         'Thiruchi':8999,
         'Thiruchirapalli':9000   
       }
data1 = pd.Series(data0)
print(data1)
print(data1['Chennai':'Thiruchirapalli'])
print(data1['Chennai'])



data3=pd.Series([1,2,3,4],index=['none','first','second','third'])
print(data3)
print(data3['third'])
print(data3['first':'third'])

import pandas as pd  #
df1 = pd.Series([0.8,0.5,8.6,7.7])
print(df1)
print(df1.values)
print(df1.index)
print(df1[1])
print(df1[0:3])

import numpy as np
df2=np.array([5,6,7,8])
print(df2)
p=pd.Series(df2)
print(p[1])
print(p[1:3])

df3 ={
         'Chennai':5000,
         'Thiruchi':8999,
         'Thiruchirapalli':9000   
       }
data1 = pd.Series(df3)
print(data1)
print(data1['Chennai':'Thiruchirapalli'])
print(data1['Chennai'])



import numpy as np
import pandas as pd
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

df = pd.DataFrame(arr2)
print(df)








