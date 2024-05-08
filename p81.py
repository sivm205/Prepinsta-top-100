#check wheather the char is vowel or consonent 

def check_vowel(char:chr):
    vowels = ['A', 'E', 'I' , 'O', 'U', 'a', 'e', 'i','o','u']
    if char in vowels:  
        return 'given character is vowels'

            
    return "given character is consonent"
    
    
val = input("enter the character\n")
print(check_vowel(val))
    

