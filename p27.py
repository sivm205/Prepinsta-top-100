#check automorphic number or not 
'''automorphic number is a number whose square ends with the number itself such as 5,6,25,76,376,890625, etc.'''

def automorphic(number:int):
    prod = number*number
    if str(number) in str(prod):
        return True
    return False


inp1 = int(input("Enter a number: "))
print(automorphic(inp1), )