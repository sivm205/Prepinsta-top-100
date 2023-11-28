#replaces all the zeroes with one in a number


#using replace method
def replace_zeroes(number: int) -> int:
    # Convert the number into a string
    number_string = str(number)
    # Replace all the 0s with 1
    updated_number_string = number_string.replace('0', '1')
    # Return the string and convert it back into an integer
    return int(updated_number_string)

input_number = 102405
print(f"Input number: {replace_zeroes(input_number)}")

#---------------------------------------------Optimized--------------------------------------------------------------------------
#iterative method 

def replace_all_zeroes_with_one(number:str):
    #number = str(number)
    new_number = ''
    for i in number:
        if i =='0':
            i = '1'
            new_number+=i 
        else:
            new_number+=i 
            
    return int(new_number)

number = (input("enter the number")) 
print(replace_all_zeroes_with_one(number))