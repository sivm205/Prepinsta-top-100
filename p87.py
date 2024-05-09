#removes the vowels from the string 


def remove_vowels(string:str):
    vow = ['A', 'E', 'I', 'O', 'U']
    new_string = ''
    for i in string:
        if i.upper() not in vow:
            new_string+=i 
            
    return new_string
    
if __name__ =='__main__':
    var = input()
    print(remove_vowels(var))
        