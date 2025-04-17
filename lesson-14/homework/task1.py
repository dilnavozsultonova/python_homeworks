import numpy as np
arr=[32, 68, 100, 212, 77]
@np.vectorize
def frantosel(x):
    c=(x-32)*5/9
    return c

numarr=frantosel(np.array(arr))
print(numarr)