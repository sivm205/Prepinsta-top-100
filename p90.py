#remove extra spaces from the string
String = "PrepInsta is fabulous"
new_string = ''
for i in String:
    if i!=' ':
        new_string+=i
        
        
print(new_string)

#-------------------------------------------

#Use join function 
String = "".join(String.split()) 

print("After removing spaces string is :",String)