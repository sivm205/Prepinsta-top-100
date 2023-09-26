#finding a prime number or not

def get_prime_number(number:int):
    if number<2:
        return True
    for i in range(2, number//2 +1):
        if number%i ==0:
            return True
            

    
inp1 = int(input("Enter the number: "))
if inp1<0:
    print("enter the possitive number")
    exit()

if get_prime_number(inp1):
    print(f"{inp1} is not a prime number")
else:
    print(f"{inp1} is a prime number")