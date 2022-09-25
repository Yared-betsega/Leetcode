class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        def check(start, src):
            if len(src) > len(s) - start:
                return False
            for i in range(len(src)):
                if src[i] != s[start]:
                    return False
                start += 1
            return True
        
        replacement = {}
        for i in range(len(indices)):
            if check(indices[i], sources[i]):
                replacement[indices[i]] = [len(sources[i]), targets[i]]
        
        ans = ""
        i = 0
        while i < len(s):
            if i in replacement:
                ans += replacement[i][1]
                i += replacement[i][0]
            else:
                ans += s[i]
                i += 1
        return ans
                