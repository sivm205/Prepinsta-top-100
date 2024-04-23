#removes duplicates element from the array

import numpy as np 

def get_unique(arr):
    if len(arr)==0 and len(arr) ==1:
        return False
    return set(arr)
    
arr = np.random.randint(1,10,size=10)
print("Before removing duplicates\n",arr)
print('after removing duplicates\n')
value = get_unique(arr)
print(value)