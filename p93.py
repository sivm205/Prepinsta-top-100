#program to capitalize the first and last letter of each word of a string

def get_capitalise(string:str):
    new_string = ""
    new_string +=(string[:1]).upper() 
    new_string += string[1:-1]
    new_string +=(string[-1]).upper()
    return new_string 
    
if __name__=='__main__':
    var = "shivam"
    print(get_capitalise(var))


