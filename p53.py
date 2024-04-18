#largest element in the array
import numpy as np

def max_element(lst):
    return max(lst)


def max_element_iter(lst):
    for i in range(0,len((lst))):
        for j in range(0, len((lst))):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
            

    return sorted(lst) 


lst = np.random.randint(1,10, size=10)
print("before sorting the array\n", lst)
print("after sorting the array\n")

array = max_element_iter(lst )
print(array[-1])

