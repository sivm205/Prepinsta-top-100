#reverse an array

import numpy as np 

def get_reverse(arr:np.array):


    i, j = 0, len(arr)-1
    while(i<j):
        temp = arr[j]
        arr[j] = arr[i]
        arr[i]  = temp 

        i+=1
        j-=1
    

    return arr

arr = np.random.randint(1,100, size=10)
print(arr)
print(get_reverse(arr))
#_________________________________

def get_reverse(arr): #using slicing 
    return arr[::-1]

print(get_reverse(arr))
        