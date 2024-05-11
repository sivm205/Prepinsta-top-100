#program to Calculate Frequency of a Characters in a String

def count_char_frequency(String):
    count = {}
    for i in String:
        if i in count:
            count[i]+=1 
        else:
            count[i]=1 
            
    return count 
    
if __name__=='__main__':
    inp1   = input()
    print(count_char_frequency(inp1))
    
#----------------------------------------------

def get_frequency(string):
    res = {i:string.count(i) for i in set(string)}
    return res 
    
print(get_frequency(inp1))