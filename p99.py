#replace a specify word with a another word

def replace_substring(string, old ,new):

    if old not in string:
        return False
        
    new_string = []
    string = string.lower()
    string = string.split()
    old.lower(), new.lower()
    for i in string:
        if i==old:
            new_string.append(new) 
        else:
            new_string.append(i) 
            
    return new_string 
    
    
if __name__=='__main__':
    inp1  = "hey Shivam Mishra" #input("enter the string\n")
    inp2 =  "shivani"        #input("enter the string want to replaced\n")
    inp3 =  'shivam'    #input("enter the new string ")
    new_string = replace_substring(inp1, inp2, inp3)
    if new_string:
        print(' '.join(new_string))
    else:
        print("please enter the correct input")

    
#-------------------------------------------
#using the replace method
def replace_substring(string, old ,new):
    return string.replace(old, new)
print(replace_substring("hey! Shivam Mishra", "shivam", "shivani"))