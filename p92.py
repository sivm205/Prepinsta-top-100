#program to count the sum of number in the string

def count_sum(string):
    sum = 0
    numbers = [1,2,3,4,5,6,7,8,9,0]
    for i in string:
        if i in str(numbers):
            sum+=int(i)
            
    return sum



    
string = '4PREP2INSTAA6'
print(count_sum(string))