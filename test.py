import numpy as np
A = np.arange(42)
A.shape = [7, 6]
print(A)
b = np.ravel(A)
print(b)
