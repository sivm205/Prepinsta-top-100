#return the longest palindrome from the array 

class CheckLargestPalindrome:
        
    def check_palindrome(self, string):
        return string == string[::-1]
        
    def get_longest_palindrome(self, arr):
        longest_pal = ''
        for i in range(len(arr)):
            if self.check_palindrome(str(arr[i])):
                if len(longest_pal) < len(str(arr[i])):
                    longest_pal = str(arr[i])
          

                    
        return len(longest_pal) 
        
        
arr = [1, 232, 5545455, 909090, 161]
p1 = CheckLargestPalindrome()
#print(p1.get_longest_palindrome(arr))
# Generate test cases
test_cases = [
    [1, 232, 5545455, 909090, 161],  # Example case with multiple palindromes
    [123, 456, 789],  # No palindromes in the array
    [111, 222, 333, 444, 555],  # All elements are palindromes
    [12, 34, 56, 78, 90],  # No palindromes in the array
    [121, 232, '', 454, 565],
      [1, 212, '', 123, 32123]  # All elements are palindromes
]

# Test the get_longest_palindrome function with the test cases
for arr in test_cases:
    p1 = CheckLargestPalindrome()
    longest_palindrome = p1.get_longest_palindrome(arr)
    print(f"Longest palindrome in {arr}: {longest_palindrome}")