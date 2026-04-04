import numpy as np
import pandas as pd
# arr=np.array([1,2,3,4,5])
# print(arr) 

# arr=np.array([[1,2,3,4],
#              [5,6,7,8]])
# print(arr)

# arr=np.arange(1,10,2)
# print(arr)

# arr1=np.linspace(0,1,5)
# arr=np.eye(4)
# print(arr)

# arr = np.array([[1,2,3],[4,5,6]])
# print(arr.shape)
# print(arr.ndim)
# print(arr.size)
# print(arr.dtype)

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a**2)

# arr = np.array([1,2,3,4,5,6])
# arr2=arr[arr>3]=100
# print(arr2)

# a=np.random.rand(2,3)
# print(a)
# b=np.random.randint(1,10,5)
# print(b)

# arr = np.array([3,1,2,3,2])
# a=np.sort(arr)
# print(a)
# b=np.unique(arr)
# print(b)

# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# help=np.dot(a,b)

# arr=np.array([[1,2,3],
#               [4,5,6]])
# print(np.sum(arr,axis=1)) #row wise
# print(np.sum(arr,axis=0)) # col wise

# a=np.array([1,2,3])
# b=a
# c=a.copy()
# b[0]=20    #b is reference of a so the value of a will also change 
# print(a)
# c[0]=100
# print(c)   # as the elements of a has been copied to new var c 
             # this is now a new array so array a will be totaly unchanged

# arr=np.array([1,2,np.nan,4])
# a=np.isnan(arr)
# b=np.nanmean(arr)
# c=np.nan_to_num(arr)
# print(a)
# print(b)
# print(c)

data=np.array([10,20,30,40,50])
normalized=(data-np.min(data))/(np.max(data)) - np.min(data)
print(normalized)