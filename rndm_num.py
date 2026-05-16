import numpy as np

rng= np.random.default_rng(seed=1)#seed=1 repeative random no
np.random.seed(seed=1)
print(rng.integers(low=1,high=7,size=(3,2)))
print(np.random.uniform(low=-1 ,high=1,size=(3,3,3)))
      