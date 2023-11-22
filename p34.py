#program to convert hexadecimal to decimal 

def get_decimal_from_hec(inp):
    l = len(inp)
    
    power = 0
    tot = 0
    for i in range(l-1,-1,-1):
        if '1' <= inp[i]<='9':
            
            tot = tot +( (16**power)*int(inp[i]))
            power+=1 
            
        else:
            num = ord(inp[i])-55 #ord is a function that returns a ascii value of a string (For A = 65 ) 
            tot = tot + (num*(16**power))
            power+=1 
            
            
    return tot 
    
print(get_decimal_from_hec('C9'))
            