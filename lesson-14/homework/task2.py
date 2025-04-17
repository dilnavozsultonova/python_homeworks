import numpy as np
arr1=np.array([2, 3, 4, 5])
arr2=np.array([1, 2, 3, 4])

@np.vectorize
def calc_pow(a,b):
    c=a**b
    return c
pow2=calc_pow(arr1,arr2)
print(pow2)


