#get the sum of array element

import numpy as np 

def get_sum(arr:np.array):
    sum = 0
    for i in arr:
        sum+=i 

    return sum 

arr = np.random.randint(1,100, size=10)
print(arr)
print(sum(arr))
print(get_sum(arr))
