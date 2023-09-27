#prime number withing a given range


def validate_prime(number:int):
    if number < 2 :
        return True
    for i in range(2, number//2 +1):
        if number % i ==0:
            return True 
        

def get_prime(num1, num2):
    for i in range(num1, num2+1):
        if validate_prime(i):
            print(f"{i} is not a prime number")
        else:
            print(f"{i} is a prime number")


inp1 = int(input("enter the first number: "))
inp2 = int(input("enter the second number: "))

get_prime(inp1, inp2)
