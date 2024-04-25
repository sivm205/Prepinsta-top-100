#get the sysmmetry pair in an array

def get_symmetry_array(array):
    set_array = set()
    temp_array = []
    
    for (i,j) in array:
        if (i,j) not in set_array:
            set_array.add((i,j))
        
        if (j,i) in set_array:
            temp_array.append((i,j))
            
    return temp_array 
    
array = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
print(get_symmetry_array(array))
