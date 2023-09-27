#armstrong number within a given range

def validate_armstrong(number):
    power = len(str(number))
    return number == sum(int(digit)**power for digit in str(number))
        
def get_armstrong(n1, n2):
    for i in range(n1, n2+1):
        if validate_armstrong(i):
            print(i)
        
        
inp1 = int(input("enter the first number:"))
inp2 = int(input("enter the second number:"))

get_armstrong(inp1, inp2)