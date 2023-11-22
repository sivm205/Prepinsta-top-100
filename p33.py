# Algorithm: Convert Octal to Decimal

def convert_octal_decimal(number):
    power = 0
    dec = 0
    while(number>0):
        dec = dec + number%10 * (8**power)
        power+=1 
        number//=10 
        
        
    return dec 
    
number = 512 

print(convert_octal_decimal(number))