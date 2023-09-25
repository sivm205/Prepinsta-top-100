#find the odd number from the given number


def find_odd(num):
    return "Not an odd" if num % 2 == 0 else "odd number"

num = int(input("Enter a number: "))
var = find_odd(num)
print(var)