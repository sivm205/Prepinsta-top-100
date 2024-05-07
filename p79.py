#program to find Equilibrium index of an array


def get_index(array):
    
    index = []
    for i in range(len(array)):
        left_sum = 0
        right_sum = 0
       
        for j in range(0, i):
            left_sum = left_sum+array[j]
        for k in range(i+1, len(array)):
            right_sum = right_sum+array[k]
            
            
        if left_sum == right_sum :
            index.append(i)
            
    return index 
    
arr = [-7,1,5,2,-4,3,0]
print(get_index(arr))
            
            
#__________________________________________________optimised__________________________________________________________________

def get_index(array):
        
        index = []
        for i in range(len(array)):
            left_sum = sum(array[:i])
            right_sum = sum(array[i+1:])
            
            if left_sum == right_sum :
                index.append(i)
                
        return index

arr = [-7,1,5,2,-4,3,0] 
print(get_index(arr))
