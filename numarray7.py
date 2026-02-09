# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 14:54:44 2025

@author: cstb31
"""

import numpy as np
arr=np.array([1,4,3,5,2])
print(arr)
print(type(arr))
print(np.__version__)
farr=np.array([3.4,1,2])
print(farr)
a=np.array([1,2,3],dtype=np.float32)
print(a)
print(a.dtype)
a=np.array([1,2,3],dtype=np.float32)
print(a)
print(a.dtype)
arr1=np.array([1,4,3,5,2])
print(type(arr1))
print(arr1.shape)
arr2=np.array([
    [1,2,3],
    [4,5,6]
    ])
print(arr2)
print(arr2.shape)

arr3=np.array([
    [[1,2,3],
     [4,5,6]],
    [[7,8,9],
     [9,7,5]]
    ])
print(arr3)
print(arr3.shape)