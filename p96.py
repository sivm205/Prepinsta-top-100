#program to check anagram between two string 
'''An anagram is a word or phrase that is created by rearranging the letters of another word or phrase,
usually using all the original letters exactly once. For example, the word "secure" is an anagram of "rescue"'''


def check_anagram(string1, string2):
    if len(string2) != len(string1):
        return False 
    string1 = string1.upper()
    string2 = string2.upper()
    string1 = set(string1)
    string2 = set(string2)
    flag = 0  
    for i in set(string1):
        for j in set(string2):
            if i==j:
                flag+=1 
                
    return len(string2) == flag 

if __name__=='__main__':       
    X, Y = 'Secure' , 'Rescue'
    print(check_anagram(X,Y))
                

#___________________________________________________optimised________________________________

def check_anagram_sort(string1, string2):
    if len(string2) != len(string1):
        return False
    string1, string2 = sorted(string1.upper()) , sorted(string2.upper())
    
    return string1 == string2
    
 

if __name__=='__main__':
    X, Y = 'Listen' , 'Silent'
    print(check_anagram_sort(X,Y))
