import numpy as np

#aggeregate means total
arr=np.array([[1,2,3,4,5],
              [6,7,8,9,10]])

print(np.sum(arr)) 
print(np.mean(arr))
print(np.std(arr))#standard deviation
print(np.var(arr))#variance=stddev**2
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))#return minimums loactaion
print(np.argmax(arr))

print(np.sum(arr,axis=0))#across column
print(np.sum(arr,axis=1))#across row

"aggeregate function sumarize data and typically return a single value"