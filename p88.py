#print the given string in reverse order 


#using reverse traversing 
string = "Hello world"
new_string = ""
for i in range(len(string)-1, -1, -1):
    new_string+=string[i]
    
print(new_string)


#using slicing 
print(new_string[::-1])
    