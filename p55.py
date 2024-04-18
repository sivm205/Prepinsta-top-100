#find the smallest and largest element from the array

import numpy as np
def find_extreme_values(arr:np.array):
    min_element = arr[0]
    for i in range(0,len(arr)):
        if arr[i]<min_element:
            min_element = arr[i] 

    return min_element, max(arr)


arr = np.random.randint(1,100,size=10)
print(arr)
print("extreme values are as follows\n",find_extreme_values(arr))