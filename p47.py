 
def calculate_number_of_digit(number:int):
    count = 0
    for i in str(number):
        count+=1

    return count

print(calculate_number_of_digit(1234))


