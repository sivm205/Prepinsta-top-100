#check the strong number
'''Strong number is a special number whose sum of the factorial of digits is equal to the original number.
 For Example: 145 is strong number. Since, 1! + 4! + 5!'''


def check_strong_number(number:int):
    sum = 0
    for i in str(number):
        sum = sum+ facto(int(i))

    if sum == number:
        return "strong number"
    else:   
        return "Not an strong number"


'''def get_factorial(number:int):       #recursive approach
    if number==1:
        return 1
    else: 
        return number*get_factorial(number-1)'''


def facto(number:int):      #to prevent function from the maximum recusrion depth error
    fact = 1
    for i in range(1, number+1):
        fact*=i
    return fact


inp1 = int(input("enter the number: "))
print(check_strong_number(inp1))
