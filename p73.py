# Function to check the disjoint presence of two arrays
def check_disjoint(array1, array2):
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                return False
    return True

import numpy as np

var1 = np.random.randint(1, 20, size=5)
var2 = np.random.randint(1, 10, size=5)

print("Array 1:", var1)
print("Array 2:", var2)
print("Disjoint presence:", check_disjoint(var1, var2))


#____________________________________________________________________________________________________________________


def check_disjoint_2(array1, array2):
    my_set = set(array1)
    for i in array2:
        if i in my_set:
            return False
    return True

print("Array 1:", var1)
print("Array 2:", var2)
print("Disjoint presence:", check_disjoint_2(var1, var2))
