#program to determine can all numbers of an array be made equal


def equal_numbers(arr):
    for i in range(len(arr)):
        # Divide number by 2
        while arr[i] % 2 == 0:
            arr[i] //= 2
        
        # Divide number by 3
        while arr[i] % 3 == 0:
            arr[i] //= 3
        
        if arr[i] != arr[0]:
            return False
    
    return True

# Driver code
if __name__ == "__main__":
    arr = [50, 75, 100]
    if equal_numbers(arr):
        print("Yes")
    else:
        print("No")
