class Solution:
    def countVowelPermutation(self, n: int) -> int:
        follower = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"]
        }
        @lru_cache
        def dfs(letter, count):
            if count == n:
                return 1
            ans = 0
            for item in follower[letter]:
                ans += dfs(item, count + 1)
            return ans
        ans = 0
        for letter in follower:
            ans += dfs(letter, 1)
            
        return ans % (10**9 + 7)
            