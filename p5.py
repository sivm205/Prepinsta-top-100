#sum of n natural numbers between a range
import numpy as np
#brute force
val1 = int(input("Enter a number: "))
val2 = int(input("Enter a number: "))
sum = 0
for i in range(val1, val2+1):
    sum = sum + i


print(sum)


#using lambda function

sum_of_range = lambda x,y : np.sum(range(x,y+1))
val11 = int(input("Enter a number: "))
val21 = int(input("Enter a number: "))
print(sum_of_range(val11, val21))
