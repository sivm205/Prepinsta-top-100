#Python Program to Replace each element by its Rank in the given Array

def Get_rank(Array):
    temp = []
    temp_arr = Array.copy()
    temp_arr.sort()
    for i in range(len(Array)):
        for j in range(len(Array)):
            if Array[i] == temp_arr[j]:
                temp.append(j+1)
                
    return temp 
    
    
arr = [100, 2, 70, 12 , 90]
print(Get_rank(arr))

#-----------------------------------------------------------optimised------------------------------------------------------------

def get_rank_using_map(array):
    temp_dict = {}
    temp_arr = array.copy()
    temp_arr.sort()
    
    for i in range(len(array)):
        if array[i] not in temp_dict:
            temp_dict[array[i]] = temp_arr.index(array[i])
        
    return temp_dict
print(get_rank_using_map(arr).values())
