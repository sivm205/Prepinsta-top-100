#count the occurance of a digit in a given numner/string 

def count_digit(number:int, digit):
    count = 0
    for i in str(number):
        if int(i) ==digit:
            count+=1

    return count 


print(count_digit(12321221,2))
