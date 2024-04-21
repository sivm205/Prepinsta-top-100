#sort the first half in ascending order and second half in descending
import numpy as np
def sorting_asc_dsc(array):
    length = len(array)
    array = sorted(array)
    print(array)
    temp_array = []
    for i in range(0, length//2):
        temp_array.append(array[i])
    for k in range(length-1, length//2 - 1, -1):
        temp_array.append(array[k])
        


    return temp_array 
arr = np.random.randint(1,100,size=10)
print("before arrangement\n", arr)
#print('After arrangement\n',sorting_asc_dsc(arr))

print(sorting_asc_dsc([1,2,4,9,7,5]))

#-----------------------------------------------------------------

#optimised 

def sorting_asc_dsc(array):
    # Sort the array
    array.sort()
    
    # Find the middle index
    mid = len(array) // 2

    # Sort the first half in ascending order and the second half in descending order
    return array[:mid] + array[mid:][::-1]