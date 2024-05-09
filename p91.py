#removes brackets from the algebric expression 

'''Example 1
Input is as follows:(x+y)+(z+q)

String without bracket is: x+y+z+q

Example 2
Input is as follows: (x-y+z)-p+q

String without bracket is: x-y+z-p+q

Example 3
Input is as follows: (a-b)+[c*d]+{e/f}
String without bracket is a-b+c*d+e/'''


def remove_brackets(string:str):
    brackets = ['(', ')', '{','}', '[',']' ]
    new_expresion = ''
    for i in string:
        if i not in brackets:
            new_expresion+=i
            
            
    return new_expresion 
    
print(remove_brackets('(a-b)+[c*d]+{e/f}'))

#-----------------------------------------------

#Using replace function
def remove_brackets(string:str):
    brackets = ['(', ')', '{','}', '[',']' ]
    for i in brackets:
        string = string.replace(i, '')
        
    return string

print(remove_brackets('(a-b)+[c*d]+{e/f}'))