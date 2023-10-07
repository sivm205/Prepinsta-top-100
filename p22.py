#get the prime factors of a number

def get_prime_number(number:int):
    for i in range(2, number//2):
        if number%i==0:
            return False
    return True



def get_factors(number:int):
    list_f = []
    for i in range(2, number):
        if number%i==0:
            list_f.append(i)
    return list_f


inp = int(input("enter the number: "))
factors = get_factors(inp)
print(f"factors are as follows {factors}",end=" ")

print("\nprime factor are as follows: ")
for i in factors:
    if get_prime_number(i):
        print(i, end=' ')


