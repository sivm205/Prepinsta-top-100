#greatest of three numbers
inp1 = int(input("Enter the first number: "));
inp2 = int(input("Enter the second number: "))
inp3 = int(input("Enter the third number: "))


def greatest_of_three_number(num1, num2, num3):
    return max(num1, num2, num3)

print(greatest_of_three_number(inp1, inp2, inp3))