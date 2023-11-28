#combination : choosing r objects out of n objects ( order is not important as ab and ba is same object)
# lets say how many people shook hand in a party in such case order is not important as a an b shook hand is same as b and a shook hand
''' ncr = n!/ (r! * (n-r)!)
    n*(n-1)/2  this is the direct formula for combination '''

def get_combination(number:int):
    ls = 0
    for i in range(1, number+1):
        for j in range(i+1, number+1):
            ls+=1 
            
    return ls 
    
    
print(get_combination(8))
        
#---------------------------------------------Optimized--------------------------------------------------------------------------

def get_combination(number: int) -> int:
    # Use the formula for calculating the number of handshakes
    # n * (n - 1) / 2
    return number * (number - 1) // 2

if __name__ == "__main__":
    number_of_people = 8
    number_of_handshakes = get_combination(number_of_people)
    print(f"Number of handshakes: {number_of_handshakes}")

                    
