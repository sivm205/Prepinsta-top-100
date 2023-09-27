#palindrome of a number

def get_palindrome(variable):
    if variable == str(variable)[::-1]:
        return "input is a palindrome"
    return "input is not a palindrome"
    
inp1 = input("enter the input: ")
print(get_palindrome(inp1))
