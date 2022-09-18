class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        ans = []
        
        count = Counter(p)
        curCount = Counter(s[:len(p)])
        if count == curCount:
            ans.append(0)
        for i in range(1, len(s) - len(p) + 1):
            curCount[s[i - 1]] -= 1
            curCount[s[i + len(p) - 1]] += 1
            if curCount == count:
                ans.append(i)
        return ans

                
                
                
                
      