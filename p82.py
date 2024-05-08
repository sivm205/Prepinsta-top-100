#check given character is alphabat or not 

def check_alpha(character:chr):
    
    #ord function return the unicode of the given character and chr gives the character of the given unicode
    if 65<= ord(character) <=90 or 97 <=ord(character)<=122:
        return 'given character is a alphabat'
        
    return 'given character is not a alphabat'
    
    

if __name__ == "__main__":  
    for i in range(65, 78):
        print(check_alpha(chr(i)))
    
     