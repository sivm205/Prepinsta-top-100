 
    
def replace_substring(x,y,z):
    new_string = ''
    flag = 0
    for i in x:
        if i!=y:
            new_string+=i 
        else:
            new_string+=z
            
            

    return new_string

if __name__=='__main__':
    x,y,z = map(str, input().split())
    print(replace_substring(x,y,z))



def replace_substring_iterative(main_string, old_substring, new_substring):
    result = ""
    i = 0
    while i < len(main_string):
        if main_string[i:i+len(old_substring)] == old_substring:
            result += new_substring
            i += len(old_substring)
        else:
            result += main_string[i]
            i += 1
    return result

# Example usage:
input_string = "PrepInsta"
old_substring = "Insta"
new_substring = "Ster"

output_string = replace_substring_iterative(input_string, old_substring, new_substring)
print(output_string)
