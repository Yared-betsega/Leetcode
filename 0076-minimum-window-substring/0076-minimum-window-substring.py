class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check():
            for i in tcount:
                if tcount[i] > scount[i]:
                    return False
            return True
        
        tcount = Counter(t)
        uni = set(t)
        scount = defaultdict(int)
        l = r = 0
        ans = [float("inf"), (-1, -1)]
        while r < len(s):
            while l < r:
                if s[l] not in uni:
                    l += 1
                elif s[l] in uni and tcount[s[l]] < scount[s[l]]:
                    scount[s[l]] -= 1
                    l += 1
                else:
                    break
            scount[s[r]] += 1
            
            if check():
                ans = min([r - l + 1, (l, r)], ans)
                while l < r and check():
                    scount[s[l]] -= 1
                    l += 1
                
            r += 1
        
        return s[ans[1][0]: ans[1][1] + 1]