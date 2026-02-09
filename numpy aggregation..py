"""
NUMPY AGGREGATION FUNTION 
"""

import numpy as np
arr = np.array([2,3,4,5])
arr2 = np.array([[2,3,4,],[6,7,8]])
arr3=([0,10,20,30,40,48,50,60,70,80,90,100])
print(np.sum(arr))
print(np.min(arr))
print(np.prod(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.sum(arr2 ,axis=1))
print(np.sum(arr2 ,axis=0))
print(np.prod(arr2 ,axis=0))
print(np.prod(arr2 ,axis=1))
print(np.mean(arr2 ,axis=0))
print(np.mean(arr2 ,axis=1))
print(np.cumsum(arr))
print(np.argmin(arr))
print(np.argmax(arr))
print(np.percentile(arr3,40))
print(np.cumprod(arr))
print(np.var(arr))

