import numpy as np

a = np.array([
    [11,22,33],
    [44,55,66],
    [77,88,99]
])
#First column
print(a[:,0])


#last row
print(a[-1])


#given data
print(a[0:2,1:3])