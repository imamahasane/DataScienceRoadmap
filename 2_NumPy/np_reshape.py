import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
print(a.shape)

re = a.reshape(2, 3)
print(re)
print(re.shape)