#Finding Sum of Minimum Absolute Difference of Array using Python
import numpy as np

def find_abs_min_difference(Array):
    
    #sorting is optional 
    lst = []
    for i in range(len(Array)): # this loop will iterate for all the element
        res = 0
        for j in range(len(Array)): #this loop use to find the difference with each element
            res = res + abs(Array[i] - Array[j])
            
        lst.append(res) 
        
        
    return min(lst)
    
size = np.random.randint(1,10)
arr = np.random.randint(1,10,size=size)
print("this are the array elements",arr)
print("Mimimum Absolute difference of an array are:",find_abs_min_difference(arr))



#______________________________________________________OPTIMISED____________________________________________________________________

