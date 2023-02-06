class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        def checkPref(word):
            if len(pref) > len(word):
                return False
            for i in range(len(pref)):
                if pref[i] != word[i]:
                    return False
            return True
    
        ans = 0
        for word in words:
            ans += checkPref(word)
        
        return ans