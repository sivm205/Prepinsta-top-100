#abundant number
''' a number is called abundant if the sum of its proper divisors is greater than the number itself such as  '''

def check_abendant(number:int):
    sum = 0
    for i in range(1,number):
        if number%i==0:
            sum+=i

    if sum>number:
        return True
    return False


inp1 = int(input("enter the number:"))
print(check_abendant(inp1))