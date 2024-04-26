#get the maximum product of sub array


def get_prod(array): #it will product a subarray elements and return a total product
    prod = 1 
    for i in array:
        prod= prod*i 
    return prod

def maximum_subarray_product(array):
    #first get the subarray in a separate list 
    subarray = []
    product = []
    
    for i in range(len(array)):  #fetch all the possible subarrays
        for j in range(i,len(array)):
            subarray.append((array[i:j+1]))
            
    for i in subarray:
        product.append(get_prod(i))
        
        
    return product
        
            
arr = [ 1, -2, -3, 0, 7, -8, -2 ]
print(maximum_subarray_product(arr))
print(max(maximum_subarray_product(arr))) #get the maximum product of subarray

#____________________________________________________________________________________________________________________

def maximum_subarray_product(arr):  #using dynamic and optimised method
    if not arr:
        return None

    max_ending_here = min_ending_here = max_so_far = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here

        max_ending_here = max(arr[i], max_ending_here * arr[i])
        min_ending_here = min(arr[i], min_ending_here * arr[i])

        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far



        