#perfet number 
'''perfect number is the number whose sum of a factorrs is equsl to the number itself   ''' 

def check_perfect(number:int):
    list = []
    for i in range(1, number+1):
        if number%i == 0:
            list.append(i)

    return sum(list) == number


inp1 = int(input("enter the possitive number:"))
if inp1 <0:
    print("enter the possitive number")
    exit()

if check_perfect(inp1):
    print(f"{inp1} is a perfect number")
else:   
    print(f"{inp1} is not a perfect number")

#--------------------------------------------------------------------------------

