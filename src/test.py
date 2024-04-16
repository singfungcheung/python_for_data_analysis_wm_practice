import numpy as np

x = np.arange(10).reshape((5, 2))
print(np.sum(x))
print(x.sum())
print(x)

print(x.mean(axis=1))
print(x.mean(axis=0))