#factorial of a number

def factorial(number:int):
    if number<=1:
        return 1
    
    else: 
        return number*factorial(number-1)
    
print(factorial(5))

#_____________________________________

#iterative approach

def factorial(number:int):
    temp = 1
    for i in range(1, number+1):
        temp = i*temp

    return temp

print(factorial(5))