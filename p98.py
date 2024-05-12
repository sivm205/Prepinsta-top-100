#Program to Count Common Subsequence in two Strings

def get_intersection(ls1 , ls2):
    common_elemts = set(ls1) & set(ls2)
    return common_elemts


def count_subsequences(str1, str2):
    Subsequence_str1 = []
    Subsequence_str2 = []
    
    for i in range(len(str1)):
        for j in range(i, len(str1)):
            Subsequence_str1.append(str1[i:j+1])
            
    for i in range(len(str2)):
        for j in range(i, len(str2)):
            Subsequence_str2.append(str2[i:j+1])
            
    
    common_elemts = get_intersection(Subsequence_str1, Subsequence_str2)
    
    return common_elemts 
    
str1 = 'ABC'
str2 = "AB"
print(count_subsequences(str1,str2), len(count_subsequences(str2, str1)))
    