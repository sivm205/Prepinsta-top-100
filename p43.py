#Can A Number Be Expressed As A Sum Of Two Prime Numbers? | Python Program

def get_prime(number:int):
    if number<=1:
        return 1
    for i in range(2, number//2+1):
        if number%i ==0:
            return True 
    return False


def check_sum(var, num):
    sum = 0
    for i in var:
        for j in var:
            sum = i+(j+1)
            if sum==num:
                return sum 
            
    return False
    
    
lst = []

        
inp1 = int(input("enter the number\n"))
for i in range(1,inp1+1):
    if get_prime(i)== False:
        lst.append(i)
        
if check_sum(lst, inp1 ) == inp1:
    print("yes possible")
else:
    print("not possible")