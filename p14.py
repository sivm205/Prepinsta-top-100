#armstrong number

def check_armstrong(number:int):
    if type(number)==float:
        return False
    sum = 0
    temp = number
    power = len(str(number))
    while(number>0):
        rem = number%10
        sum = sum + (rem**power)
        number//=10
        
    if temp == sum:
        return True
    return False
    
    
inp1 = int(input("enter the integer number: "))
if(check_armstrong(inp1)):
    print(f"{inp1} is a armstrong number")
else:
    print(f"{inp1} not an armstrong number")

#_____________________________________________________optimized__________________________________________________________

def check_armstrong(number):
    power = len(str(number))
    return number == sum(int(digit)**power for digit in str(number))

inp1 = int(input("Enter an integer number: "))
if check_armstrong(inp1):
    print(f"{inp1} is an Armstrong number")
else:
    print(f"{inp1} is not an Armstrong number")