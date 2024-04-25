#maximize the dot product of two vectors
'''If the vectors are both in ascending order or both in descending order, each element of one vector is multiplied by a relatively large element of the other vector, 
resulting in a larger product'''

import numpy as np
def get_maximum_scalar(arr1,arr2):
    prod = 0
    arr1 = np.sort(arr1)
    arr2 = np.sort(arr2)
    
    for i in range(len(arr2)):
        prod = prod+ (arr1[i]*arr2[i])
        
    return prod

arr1 = np.random.randint(1,10,size=10)
arr2 = np.random.randint(1,10,size=10)
print(get_maximum_scalar(arr1,arr2))
