#finding a year leap year or not

def find_leap_year(year:int):
    if year%400 == 0:
        return True
    elif year%4 ==0 and year%100!=0:
        return True
    
    else:
        return False
    
year = int(input("Enter the year: "))
if find_leap_year(year):
    print(f"{year} is a leap year")

