#fibonacci series

def fibo_series(number :int):
    n1 , n2 = 0 , 1
    print(n1, n2, end=' ')
    for i in range(2,number):
        n3 = n1 + n2 
        
        n1 = n2
        n2 = n3
        print(n3,end=' ')
        

inp = int(input("enter the number: "))
fibo_series(inp)  
print("\n")  
#___________________________________________________________

# recursive approach

def fibo_series(number:int):
    if number<=1:
        return number
    else: return (fibo_series(number-1) + fibo_series(number-2))

print("using recursive approach")
for i in range(inp):
    print(fibo_series(i), end=' ')
