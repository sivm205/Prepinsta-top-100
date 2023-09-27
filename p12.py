#reverse of a number

def reverse_of_a_number(number:int):
    return int(str(number)[::-1])

print(reverse_of_a_number(1234))




#brute force method
def reverse_number(number : int):
    rev = 0
    while(number>0):
        rem = number%10
        rev = rev*10 + rem
        number//=10

    return rev
print(reverse_number(1234))
