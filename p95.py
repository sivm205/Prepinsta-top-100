#program to find non repeating characters in a string

def non_repeated(string:str):
    count = {}
    uniq_char = []
    
    for i in string:
        if i in count:
            count[i]+=1 
        else:
            count[i]=1 
            
    for (i,j) in count.items():
        if j==1:
            uniq_char.append(i)
            
    return uniq_char 
    
String = "Hey! I am Shivam Mishra"
string1 = ' '.join(non_repeated(String))
print(string1)