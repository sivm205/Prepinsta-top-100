#to check number is a harshad number or not

''' harshad number is basically a number that is divisible by the sum of its digits'''

def sum_of_a_digit(number:int):
    sum = 0
    while(number>0):
        rem = number%10 
        sum = sum + rem
        number//=10
        
    return sum
    
def check_harshad(number:int):
    if number% sum_of_a_digit(number)==0 :
        return True
    return False
    
    
print(check_harshad(21))

#------------------------------------------------------------optimized------------------------------------------------------------

def check_harshad(number: int):
    return number % sum(int(digit) for digit in str(number)) == 0

print(check_harshad(21))