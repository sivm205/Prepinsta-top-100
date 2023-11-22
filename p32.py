#binary to decimal

    

def convert_decimal(number):
    dec = 0
    power = 0
    while(number>0):
        rem = number%10 
        dec = dec + (rem*2)**power
        power+=1
        number//=10
        
    return dec 
    
print(convert_decimal(10101))



#____________________________________________________________________________________________________________________________________

#decimal to binary

def convert_binary(number:int):
    ls = []
    while(number>0):
        ls.append(number%2)
        number//=2
        
    return ls[::-1] if ls else [0] #if number is 0 then it will return [0] else it will return the list in reverse order

print(convert_binary(21))

        
        