#calculate the frequency of element in an array 
import numpy as np 

class Count_Frequency():
    def __init__(self, arr):
        self.arr = arr 
        
    def get_frequency(self):
        temp_dict = {}
        for i in range(0, len(self.arr)):
            if self.arr[i] in temp_dict:
                temp_dict[self.arr[i]] +=1 
            else:
                temp_dict[self.arr[i]] = 1 
                
                
        return temp_dict 
        

array1 = np.random.randint(1,100,size=10)
array1 = Count_Frequency(array1)
print(array1.get_frequency())


