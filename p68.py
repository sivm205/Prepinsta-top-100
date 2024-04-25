#find the minimum scalar product of two vector
'''When 
𝑏
b is in descending order, the dot product 
𝑎
⋅
𝑏
a⋅b will be minimized because each element of 
𝑎
a will be multiplied by the largest corresponding element of 
𝑏
b, resulting in the smallest possible sum
''' 
import numpy as np 
def get_minimum_scalar(arr1,arr2):
    prod = 0
    arr1 = np.sort(arr1)
    arr2 = np.flip(np.sort(arr2))
    
    for i in range(len(arr2)):
        prod = prod+ (arr1[i]*arr2[i])
        
    return prod 
    

arr1 = [1, 2, 6, 3, 7]
arr2 = [10, 7, 45, 3, 7]

print(get_minimum_scalar(arr1,arr2))