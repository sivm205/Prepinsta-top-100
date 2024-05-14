#Print All Lexicographic Permutations in Sorted Order using Python

def lexicography(string, i=0):
    if i == len(string):
        return [''.join(string)]

    res = []
    for j in range(i, len(string)):
        string[i], string[j] = string[j], string[i]  # Swap
        res.extend(lexicography(string, i + 1))  # Generate permutations for the rest of the string
        

    return res

string = 'ABC'
print(lexicography(list(string)))

#------------------------------------------------------------------------------------------------

from itertools import permutations

def lexicography(string):
    tm_list = [''.join(p) for p in permutations(string)]
    return tm_list

string = 'ABC'
print(lexicography(string))
