import numpy as np

#2d array
arr=np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12]])

#arr[start:end:steps]
print("\n")
print(arr[0::2])

#np slicing way
print(arr[:,-1])#[r,c]    [ start:end:stop , start:end:stop  ,  start:end:stop  ] => 3d
print("\n")
print(arr[:,0::2])
