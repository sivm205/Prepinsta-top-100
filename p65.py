#Repeating elements in an Array in Python

import numpy as np 
def get_repeated_element(arr):
    '''using mapping'''
    temp_dict = {}
    temp_list = []
    for i in arr:
        if i in temp_dict:
            temp_dict[i] +=1 
        else:
            temp_dict[i] = 1 

    for key, value in temp_dict.items():
        if value>1:
            temp_list.append(key)
    return temp_list 

array = np.random.randint(1,10,size=20)
print(array)
print("repeated elements are as follows\n",get_repeated_element(array))

    
