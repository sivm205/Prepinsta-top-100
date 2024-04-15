#Python program for Converting digit/number to words

''' 1121 = one thousand one hundred twenty one ''' 


def conver_number_to_words(number:int):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    arr_2 = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty','seventy', 'eighty', 'ninty']
    arr3 = ['eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen','eighteen','ninteen']
    arr_4 = ['hundred','thousand']

    
    if len(str(number))==1:
        print(str(number) +'='+ str(arr[number]))
        
    elif len(str(number))==2:
        two_digit = number//10
        last_digit = number%10
        
        
        for i in range(1,10):
            if i==two_digit and two_digit>1 :
                print(str(arr_2[i-1]) + ' '+ str(arr[last_digit]))
                return 1 
                
            elif two_digit==1 and last_digit!=0:
                print(arr3[last_digit-1])
                return 1 
                
            elif last_digit == 0 :
                print(str(arr_2[two_digit-1]))
                return 1
            
    elif len(str(number))==3:
        first_digit = number%10
        mid_digit = number//10 %10 
        third_digit =  number//100 

        for i in range(1,11):
            if mid_digit==0 and first_digit==0 :  # 100, 200, 300 and so on to 900
                print(arr[third_digit] + ' hundred')
                return 1
                
            elif first_digit>=1 and mid_digit==0 and third_digit==1:  #101 to 109
                print("one hundred and "+ str(arr[first_digit]))
                return 1
            
            elif first_digit>=1 and mid_digit==1 and third_digit==1: #111 to 119
                print("one hundred and "+ str(arr3[first_digit-1]))
                return 1
                
            elif first_digit>=1 and mid_digit>=2 and third_digit>=1: #121 to 999
                print(str(arr[third_digit]) + ' hundred and '+ str(arr_2[mid_digit-1]) +' '+ str(arr[first_digit]))
                return 1 
                
                
            elif first_digit==0 and mid_digit>0 and third_digit>0:
                print(arr[third_digit] + ' hundred and '+ arr_2[mid_digit-1])
                return 1
            

        
    elif len(str(number)) == 4:
        first_digit = number % 10
        mid_digit = number // 10 % 10
        third_digit = number // 100 % 10
        fourth_digit = number // 1000
        
        if mid_digit == 0 and third_digit == 0 and first_digit == 0:
            print(arr[fourth_digit] + ' ' + arr_4[1])
        elif third_digit == 0 and first_digit == 0:
            print(arr[fourth_digit] + ' ' + arr_4[1] + ' and ' + arr_2[mid_digit - 1] + ' ' + arr[first_digit])
        elif mid_digit == 0 and first_digit == 0:
            print(arr[fourth_digit] + ' ' + arr_4[1] + ' and ' + arr[third_digit] + ' ' + arr_4[0])
        elif mid_digit == 0 and third_digit == 0:
            print(arr[fourth_digit] + ' ' + arr_4[1] + ' and ' + arr[first_digit])
        elif third_digit == 0:
            print(arr[fourth_digit] + ' ' + arr_4[1] + ' and ' + arr_2[mid_digit - 1] + ' ' + arr[first_digit] + ' ' + arr_4[0])
        elif mid_digit == 0:
            print(arr[fourth_digit] + ' ' + arr_4[1] + ' and ' + arr[third_digit] + ' ' + arr_4[0] + ' and ' + arr[first_digit])
        else:
            print(arr[fourth_digit] + ' ' + arr_4[1] + ' and ' + arr[third_digit] + ' ' + arr_4[0] + ' and ' + arr_2[mid_digit - 1] + ' ' + arr[first_digit])
            





conver_number_to_words(100)
conver_number_to_words(101)
conver_number_to_words(109)
conver_number_to_words(111)
conver_number_to_words(119)
conver_number_to_words(120)
conver_number_to_words(220)
conver_number_to_words(430)
conver_number_to_words(990)
conver_number_to_words(121)
conver_number_to_words(327)
conver_number_to_words(107)
conver_number_to_words(333)
conver_number_to_words(1000)
conver_number_to_words(1001)
conver_number_to_words(1010)
conver_number_to_words(1100)
conver_number_to_words(1101)
conver_number_to_words(1110)
conver_number_to_words(1111)
conver_number_to_words(1119)
conver_number_to_words(1121)