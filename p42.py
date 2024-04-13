from typing import List
#degree celsius to fahrenhit 
# 0 degree celsius  = 32 degree fahrenhit and the formula is f = c*9/5 + 32 where c is the degree celsius and f is the degree fahrenhit


def converting_Celsius_to_Fahrenheit(celsius:float):
    return celsius*9/5 + 32

inp2 = float(input("enter the degree celsius:"))
print(f"{inp2} degree celsius is equal to {converting_Celsius_to_Fahrenheit(inp2)} degree fahrenhit")

#________________________________________________________________________________________________________________________


#fahrenhit to degree celcius
# for finding the fahrenhit we reverse the formula like c = (f-32)*5/9 where f is the degree fahrenhit and c is the degree celsius


def getting_Celsius_from_Fahrenheit(fahrenheit:float):
    return (fahrenheit-32)*5/9

inp3 = float(input("enter the degree fahrenhit:"))
print(f"{inp3} degree fahrenhit is equal to {getting_Celsius_from_Fahrenheit(inp3)} degree celsius")
