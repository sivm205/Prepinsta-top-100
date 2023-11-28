#get the addition of fractions

'''Initialize variables of numerator and denominator
Take user input of two fraction
Find numerator using this condition (n1*d2) +(d1*n2 ) where n1,n2 are numerator and d1 and d2 are denominator
Find denominator using this condition (d1*d2) for lcm
Calculate GCD of a this new numerator and denominator
Display a two value of this condition x / gcd, y/gcd '''


def get_fractions_addition(num1,deno1,  num2, deno2):
    # first gettting the numerator 
    numerator = num1*deno2 + num2*deno1
    denominator = deno1*deno2 
    
    #Calculate GCD for these two number
    for i in range(1, min(numerator, denominator)):
        if numerator%i == denominator%i ==0:
            res_n = numerator//i
            res_d = denominator//i 
            
    return res_n, res_d
    
n1 , d1 , n2, d2 = 14, 10, 24, 3

rn , rd = get_fractions_addition(n1, d1, n2, d2)
print('Resultant fraction are as follows\n' , rn, '/', rd)