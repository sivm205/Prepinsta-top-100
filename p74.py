#find out if array is a subset of another array or vice-versa

# if all the elements of array 2 are found in array 1, then array 2 is said to be a subset of array 1.

def check_subset(array1, array2):
    temp_array= set(array1)
    temp_set = set()
    
    for i in array2:
        if i in temp_array:
            temp_set.add(i) 
            
            
    return len(temp_set) == len(array2)
    
import numpy as np 
import numpy as np
array1 = [1, 2, 3.0, 4, 5]
array2 = [3, 4, 6]
print(array1,array2)
if check_subset(array1,array2):
    print("Yes! array 2 are the subset of array 1")
else:
    print("array 2 are not a subset of array 1")

#______________________________________________"OPTIMISED CODE"______________________________________________________________________

def check_subset(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    
    return set2.issubset(set1)

print(array1, array2)

if check_subset(array1, array2):
    print("Yes! array 2 is a subset of array 1")
else:
    print("array 2 is not a subset of array 1")