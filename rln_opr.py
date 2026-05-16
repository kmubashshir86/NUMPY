import numpy as np

#comparisons

#individual element pair comparison
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

print(arr1<arr2)

print(arr1==1)

# [] <= subscript opr
arr1[arr1<3] = 0
print(arr1)