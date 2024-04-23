#Counting Distinct Elements in an Array
def get_distinct(arr):
    return len(set(arr))
    
arr = list(map(int, input().split()))

print(get_distinct(arr))