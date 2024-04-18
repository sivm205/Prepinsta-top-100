#find the smallest element in the array

import numpy as np

def min_element(lst:np.array):
    return min(lst)

def min_element_iter(lst:np.array):
    min_ele = lst[0]
    for i in range(0, len(lst)):
        if lst[i] < min_ele:
            min_ele = lst[i]

    return min_ele


lst = np.random.randint(1,100, size=10)
print("before sorting\n",lst)
print(min_element(lst))
print(min_element_iter(lst))