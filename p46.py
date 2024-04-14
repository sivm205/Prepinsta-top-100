# Find prime numbers between 1 to 100
def check_prime(number: int):
    if number <= 1:
        return False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
    return True

for i in range(1, 101):
    if check_prime(i):
        print(i, end=" ")
