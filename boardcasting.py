import numpy as np

"broadcasting do help to perform operations between arrays of different shapes"
arr1=np.array([[1,2,3,4]]) # row = 1 column = 4
arr2=np.array([[1],[2],[3],[4]]) # row = 4 column = 1

print(arr1.shape)
print(arr2.shape)

"""so shapes came to be (1,4) and (4,1)  1st set is ([1],4) ([4],1)  1 and 4 both are not same but one of them is one 
2nd set is (1,[4]) (4,[1])  4 and 1 both are not same but one of them is one so we can boardcast them """

print(arr1*arr2)