#couting the number of even and odd element in the array 

import numpy as np
def get_even_odd(array):
    dictionary = {}
    dictionary['even'] = 0  # Initialize 'even' key
    dictionary['odd'] = 0  # Initialize 'odd' key
    for i in range(len(array)):
        if array[i]%2==0:
            dictionary['even']+=1 
        else:
            dictionary['odd']+=1 
            
    return dictionary   
var1 = np.random.randint(1,100, size=30)
print(var1)
dictionary = get_even_odd(var1)
print(dictionary)