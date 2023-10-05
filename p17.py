#fibonacci series withing a range

def fibonacci(number:int):
    if number<=1:
        return number
    else: 
        return fibonacci(number-1) + fibonacci(number-2)
        
        
inp = int(input("enter the first number: "))
inp2 = int(input("enter the second number: "))

for i in range(inp, inp2):
    print(fibonacci(i), end=' ')
    
print("\n\n")
#___________________________________________________________

#iterative approach

def fibonacci_series_range(n1, n2):
    series = [n1, n2]
    for i in range(n1, n2):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        series.append(n3)
    return series

inp1 = int(input("enter the first number: "))
inp2 = int(input("enter the second number: "))
print(fibonacci_series_range(inp1 , inp2))

