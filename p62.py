#soring according to the occurance of the element
import numpy as np 
def sorting_by_element(arr):        #using dictionary
    temp_list = {}
    for i in arr:
        if i in temp_list:
            temp_list[i]+=  1 
        else:
            temp_list[i] =  1 
        
    return temp_list 
    
    
arr = np.random.randint(1,10,size=10)
print('before sorting=')
dictonary = sorting_by_element(arr)
print(dictonary)

temp_arr = [i for i in dictonary.values()]
temp_arr.sort()
print('after sorting=')
print(temp_arr[::-1])

#______________________________________________________optimised______________________

from collections import Counter #counter from collection method directly return a dictionary in a sorted format 
import numpy as np 
def sorting_array(arr):
    return Counter(arr)


dictionary = sorting_array(arr)
print('\nBefore sorting=',dictionary)
print('After sorting=',sorted(dictionary.values(), reverse=True))


#______________________________using list___________________________________________________

def sort_acc_elemet(array):
    temp_arr_count  = []
    array = array.tolist()
    count = 0 
    temp_arr = []
    for i in range(len(array)):
        if array[i] not in temp_arr:
            temp_arr_count.append(array.count(array[i]))
            temp_arr.append(array[i])
            
    return temp_arr_count 
    
    
sorted_array = sort_acc_elemet(arr)
sorted_array.sort()
print(sorted_array[::-1])

