#program to toggle each character in a string

def get_toggle(string:str):
    
    empty_str = ''
    for i in string:
        if i.upper() :
            empty_str+=(i.lower())
            
        empty_str+=(i.upper())
        
    return empty_str
        
if __name__ == '__main__':        
    String = 'GuDDuBHaiyA'
    print(get_toggle(String))


#___________________________________________________optimised________________________________

def get_toggle(string:str):
    return string.swapcase()


if __name__ == '__main__':      
    String = 'GuDDuBHaiyA'
    print(get_toggle(String))