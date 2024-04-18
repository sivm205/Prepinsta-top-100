#find the second smallest element from the array 

import numpy as np

def get_second_smallest(array:np.array):
    sec_smallest = 0 

    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if array[i] > array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i]  = temp


    return arr[-2] #as 


arr = np.random.randint(1,100, size=10)
print(arr)
print(get_second_smallest(arr))