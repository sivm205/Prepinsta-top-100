#H.C.F highest common factor as the name suggests common factor that are highest among all the factors of two or more numbers
#H.C.F of 36 and 60 is 12

def get_hcf(num1:int , num2:int) -> int:
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1

print(get_hcf(36, 60))
#____________________________________________________________________________________________________________________________________

def get_hcf(num1:int, num2:int):
    hcf = []
    for i in range(1, min(num2, num1)+1):
        if num1%i == num2%i ==0:
            hcf.append(i)  #or you can use temp variable to store the factor and return the last value of temp
            #temp = i

    return max(hcf)
    #return temp ;   in this way whatever the last value of temp will be returned as hcf

print(get_hcf(36, 60))

