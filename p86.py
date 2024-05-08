#count the number of vowels in a string 

def count_v(string:str):
    lst = ['A', "E", "I", "O", "U"]
    flag = 0
    
    for i in string:
        if (i.upper()) in lst:
            flag+=1 
            
            
    return flag 
    
if __name__=='__main__':
    var = input("enter the string\n")
    print(count_v(var))


