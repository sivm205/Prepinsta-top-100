#factor of a number

def get_factor_of_num(num:int):
    list = []
    for i in range(1,num+1):
        if num%i==0:
            list.append(i)

    return list

inp1 = int(input("enter the number: "))

print(get_factor_of_num(inp1))