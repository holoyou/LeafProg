import numpy as np
A = np.arange(24)
A.shape = [4, 6]
print(A)
b = np.ravel(A)
print(b)
