class Solution:
    def countVowelPermutation(self, n: int) -> int:
        follower = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"]
        }
        memo = {}
        def dfs(letter, count):
            if count == n:
                return 1
            if (letter, count) in memo:
                return memo[(letter, count)]
            ans = 0
            for item in follower[letter]:
                ans += dfs(item, count + 1)
            memo[(letter, count)] = ans
            return memo[(letter, count)]
        
        ans = 0
        for letter in follower:
            ans += dfs(letter, 1)
            
        return ans % (10**9 + 7)
            