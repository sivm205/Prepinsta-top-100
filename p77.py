#sort the first array according to the occurance of second array

def sort_first_by_second(array1, array2):
    temp_list = []
    for i in range(len(array2)):
        for j in range(len(array1)):
            if array1[j] == array2[i]:
                temp_list.append(array1[j])
                
    for i in array1:
        if i not in temp_list:
            temp_list.append(i)
            
    return temp_list
    
   
    
    
arr1 = [ 20, 1, 20, 5, 7, 1, 9, 39, 6, 18, 18 ]
arr2 = [ 20, 1, 18, 39 ]

print(sort_first_by_second(arr1, arr2))
            
            
            