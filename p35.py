#decimal to octal
def get_octal_from_decimal(number:int):
    ls = []
    
    while(number>0):
        ls.append(number%8)
        number//=8 
        
    return ls[::-1]
    
    
print(get_octal_from_decimal(973))