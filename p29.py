''' friendly pair or not - In number theory, a friendly pair is two numbers that have the same abundancy. The abundancy of a number is
 the ratio between the sum of its divisors and the number itself. For example, 6 and 28 are a friendly pair
because (1 + 2 + 3) / 6 = (1 + 2 + 4 + 7 + 14) / 28   '''


def friendly_pair(number1:int , number2:int):
    sum1, sum2 = 0, 0
    for i in range(1, number1):
        if number1 % i == 0:
            sum1 += i
    for i in range(1, number2):
        if number2%i ==0:
            sum2 += i

    if sum1/number1 == sum2/number2:
        return True
    return False


inp1 = int(input("enter the number1:"))
inp2 = int(input("enter the number2:"))
print(friendly_pair(inp1, inp2))