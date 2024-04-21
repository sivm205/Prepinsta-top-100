#sort the element of array
import numpy as np 

def sort_array(arr):
    return sorted(arr)
arr = np.random.randint(1,100, size=(20)) 
arr = sort_array(arr)
print(arr)

#using bubble sort 
import numpy as np 
arr = np.random.randint(1,100,size=10)

print(arr)
for i in range(0, len(arr)):
    for j in range(0, i+1):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            
        else:
            continue 
        
print(arr)



    