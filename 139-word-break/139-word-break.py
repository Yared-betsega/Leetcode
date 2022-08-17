class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        @lru_cache
        def dp(index):
            if index == len(s):
                return True
            
            string = ""
            for i in range(index, len(s)):
                string += s[i]
                if string in words:
                    if dp(i + 1):
                        return True
            return False
        
        return dp(0)
                    
                    
            