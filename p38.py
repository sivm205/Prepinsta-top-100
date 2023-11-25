#permutation : permutation is an arrangement of r object out of all objects ( order is important as ab and ba is two distinct object)

''' permutation = n!/ (n-r)! lets say selecting number of student in the class is 10 and only six seats is 
left then how can we arrange them ''' 


def get_permutation(N:int, R:int):
    prod = 1
    
    for i in range(N-R+1 , N+1):
        prod = prod*i 
        
    return prod
    
    
print(get_permutation(10, 6))