#remove non alphabetic characters from the string 
def remove_non_alpha(string:str):
    new_string = ''
    for i in string:
        if 65<= ord(i)>=90 or 97<=ord(i) <=122:
            new_string+=i 
            
    return new_string 
    
String1 = "#Justice!For@Chutki123"
print(remove_non_alpha(String1))