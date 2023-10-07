#perfect square number

def check_perfect_square(number:int):
    sqrt = int(number**0.5)
    if sqrt*sqrt == number:
        return True
    return False

inp1 = int(input("enter the sqaure number: "))
if check_perfect_square(inp1):
    print(f"{inp1} is a perfect square number")
else:
    print(f"{inp1} is not a perfect square number")
