class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}
        def dp(index):
            if index == len(s):
                return True
            if index in memo:
                return memo[index]
            
            string = ""
            for i in range(index, len(s)):
                string += s[i]
                if string in words:
                    if dp(i + 1):
                        memo[index] = True
                        return True
            memo[index] = False
            return False
        
        return dp(0)
                    
                    
            