#count the number of days in a given month

def count_days(month:str, year:str):
    if year%400==0 and month==2 or year%4==0 and year%100!=0 and month==2:
        print("given month has 29 days")

    elif month%2==0:
        print("given month has 31 days")
    elif month%2!=0:
        print("given month has 30 days")
    else:
        print("given month has 28 days")



count_days(12,2002)
count_days(2, 2000)
    


    





        