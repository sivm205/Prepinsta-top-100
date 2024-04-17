#counting the number of x divisors from the number

def counting_divisor(number, divisor_n):
    flag = 0
    for i in range(1, number+1):
        count = 0
        for j in range(1,i+1):
            if i%j==0:
                count +=1 
                
        if divisor_n == count:
            flag +=1 
    return flag
   
#inp1 = int(input())
#inp2 = int(input())

print(counting_divisor(10,4))

                
                