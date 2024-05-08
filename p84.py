#return the length of a string 


def get_length(string):
    return len(string)

string = 'hello world'
print(get_length(string))
#____________________________________________________________________


def get_length(string:str):
    count = 0 
    for i in string:
        count+=1 
        
    return count
    
if __name__ == "__main__":
    
    inp1 = input("enter the string\n")
    print('length of a string is: ',get_length(inp1))