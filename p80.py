#left and right rotation of elements in array by one possition

def right_roatation(array):
    
    for i in range(0,len(array)-1):
        temp = array[0]
        array[0] = array[i+1]
        array[i+1] = temp
        
        
    return array 
def left_rotation(array):
    
    for i in range(len(array)-1):
        temp = array[i+1]
        array[i+1] = array[i]
        array[i] = temp
        
    return array
    
array1 = [1,2,3,4,5]
array2 = [1,2,3,4,5]
print("right rotation",right_roatation(array1))
print("left rotation", left_rotation(array2))
        
#_________________________________________________________optimised_____________________________________________________________

def right_rotation(array):
    temp = array[-1]
    for i in range(len(array)-1,0,-1):
        array[i] = array[i-1]
    array[0] = temp
    return array

def left_rotation(array):
    temp = array[0]
    for i in range(0,len(array)-1):
        array[i] = array[i+1]
    array[-1] = temp
    return array

