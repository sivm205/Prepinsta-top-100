#greatest of two numberss

inp1 = int(input("Enter the first number: ")); 
inp2 = int(input("Enter the second number: "))

def greatest_of_two_numbers(num1, num2):
    if num2 > num1:
        return num2
    return num1

print(greatest_of_two_numbers(12, 21))
