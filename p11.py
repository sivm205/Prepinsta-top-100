#sum of a digits of a number


def sum_of_a_digit(number:int):
   if number>=0:
       if number == 0:
           return 0
       else:
           return  number%10 + sum_of_a_digit(number//10)
   else:
       return 0



def sum_of_a_digit_bf(number:int):
    sum = 0
    while(number>0):
        sum = sum+number%10
        number//=10

    return sum


inp1 = int(input("Enter the number: "))
print(sum_of_a_digit(inp1))
print(sum_of_a_digit_bf(inp1))