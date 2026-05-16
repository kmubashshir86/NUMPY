import numpy as np

#0 dimension array
arr=np.array('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
arr1=np.array("ABCDEFGHIJKLM,NOPQRSTUVWXYZ")

#output array
print(arr)

#output dimension of array
print(arr.ndim)
print(arr1.ndim)

#1d array
arr_1d = np.array(['A','B','C'])

print(arr_1d.ndim)

#2d array

arr_2d = np.array([[1,2,3],
                   ['A','B','C']])

print(arr_2d.ndim)

#3d array

arr_3d = np.array([[[1,2],[2,3]],
                   [[4,5],[6,7]]])

print(arr_3d.ndim)

#array_shape
print(arr_3d.shape)

#chain_indexing

print(arr_3d[0][0][0])

#multidimensional indexing
print(arr_3d[0,0,0])