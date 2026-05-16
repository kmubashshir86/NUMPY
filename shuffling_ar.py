import numpy as np

rng=np.random.default_rng()

arr=np.array([1,2,3,4])
rng.shuffle(arr)
print(arr)