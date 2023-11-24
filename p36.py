#octal to binary conversion 
# in this we directly can not convert into binary from octal so first convert into decimal value then convert into binary 

def convert_decimal(number:int):
    length = len(str(number))-1
    length  = int(length)
    sum = 0
    for num in str(number):
        sum = (int(num) * (8**length)) + sum
        length-=1 
        
    return sum
    
def conver_binary(number:int ):
    number = convert_decimal(number)
    lsb = []
    while(number>0):
        lsb.append(number%2)
        number//=2
        
        
    return lsb[::-1]
    
inp = 512  #octal 
print(conver_binary(inp))
#----------------------------------------------------------------------------------------------------------------------------

#optimize code
def convert_octal_to_binary(number: int) -> str:
    decimal = 0
    length = len(str(number)) - 1
    
    while number > 0:
        digit = number % 10
        decimal += digit * (8 ** length)
        length -= 1
        number //= 10
    
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
        
    return binary
    
inp = 512  # octal 
print(convert_octal_to_binary(inp))
        
        