from functools import lru_cache
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # First build the connection
        # For the case of I, since it cannot be followed by the itself, it may be followed by the other vowels
        follower = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"]
        }
        
        # Accepts the current letter and 
        # the length of the string formed till now
        
        @lru_cache
        def dfs(letter, count): 
            if count == n:
                return 1
            permutation = 0
            for item in follower[letter]:
                # Add the result of adding the next possible follower of letter
                permutation += dfs(item, count + 1)
            
            return permutation
        
        ans = 0
        # Iterate over the starting five vowels 
        # We can avoid this two lines of code by adding "": ["a", "e", "i", "o", "u"] on our hashmap
        for letter in follower:
            ans += dfs(letter, 1) # Add the result of starting from each vowel
            
        return ans % (10**9 + 7)

# time and space complexity
# time: O(n)
# space: O(n)            