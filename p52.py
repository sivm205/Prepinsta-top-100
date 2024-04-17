#finding the square root of a quadratic equation

def finding_roots(A,B,C):
    if A==0:
        print("invalid value of A")
        return 0 
    
    D = ((B**2) - 4*A*C)**0.5 
    eq_plus = (-B + D)//2*A 
    eq_minus = (-B - D)//2*A 

    if D>0:
        print('Root are real\n')
        print(eq_minus, eq_plus)

    elif D==0:
        print("both roots are real and equal\n")
        print(eq_minus, eq_plus)

    else:
        print("roots are imaginary\n")
        print(eq_minus,eq_plus)



(finding_roots(1,4,4))