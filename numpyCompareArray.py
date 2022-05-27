import numpy as np

scale = [1,0,0,0,1,0,0,0,1,0,0,0]
data1 = [8,2,0,1,0,0,1,0,1,0,0,0]
data2 = [8,0,0,0,1,0,1,0,1,0,0,0]

scale= np.array(scale, dtype=bool)
data1= np.array(data1, dtype=bool)
data2= np.array(data2, dtype=bool)

and1 = np.bitwise_and(scale, data1)
and2 = np.bitwise_and(scale, data2)

is_match1 = np.array_equal(scale, and1)
is_match2 = np.array_equal(scale, and2)

print(is_match1) # False
print(is_match2) # True