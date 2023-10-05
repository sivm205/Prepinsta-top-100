#return nth term of fibonacci series

class Fibonacci:
    def __init__(self, number:int):
        self.n1 = 0
        self.n2 = 1
        self.number = number

        for i in range(1, number):
            self.n3 = self.n1 + self.n2
            self.n1 = self.n2 
            self.n2 = self.n3

    def display(self):
        print(f"{self.number}th fibonacci number is {self.n3}")
    

inp = int(input("enter the number: "))
fibo1 = Fibonacci(inp)
fibo1.display()



#____________________________________________________________________________________-

#through recursion

class fibonacci:
    def fibo(self, number:int):
        if number<=1:
            return number
        else:
            return ( self.fibo(number-1) + self.fibo(number-2) )
        
    def display(self):
        inp = int(input("enter the number: "))
        return self.fibo(inp)
    
fib1 = fibonacci()
print(fib1.display())
    


        
        
