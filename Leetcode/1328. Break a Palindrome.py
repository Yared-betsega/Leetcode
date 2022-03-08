class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
            
        if len(palindrome) == 1:
            return ""
        
        elif palindrome == "a" * len(palindrome):
                palindrome = palindrome[:len(palindrome)-1] + "b"
                return palindrome
        
        else:
            word = palindrome
            for i in range(len(palindrome)):
                if palindrome[i] != "a":
                    palindrome = palindrome[:i] + "a" + palindrome[i+1:]
                    break
                    
            if palindrome == "a" * len(palindrome):
                palindrome = word[:len(word)-1] + "b"
                
            return palindrome
    
# time and space complexity
# time complexity = O(n)
# space complexity = O(1)
            
            
