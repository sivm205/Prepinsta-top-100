#lcm of two numbers
def lcm_of_two_numbers(num1, num2):
    for i in range(max(num1, num2), num1*num2+1):

        if i%num1 ==i%num2==0:
            return i
        else :
            return num1* num2 #incase if it dont find any lcm then it will return the product of two numbers
    
print(lcm_of_two_numbers(30,36))
    