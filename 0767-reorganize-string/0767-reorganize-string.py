class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = [i for i in range(len(s))]
        count = Counter(s)
        sor = sorted(count.items(), key = lambda x: x[1], reverse = True)
        
        start = 0
        for item in sor:
            cur = start
            for n in range(item[1]):
                if type(ans[cur]) != type(3):
                    if type(ans[cur + 1]) != type(3) or ans[cur] ==item[0]:
                        return ""
                    cur += 1
                    
                ans[cur] = item[0]
                cur = (cur + 2) % len(s)
                
            start = cur
        for i in range(1, len(ans)):
            if ans[i] == ans[i - 1]:
                return ""
        return "".join(ans)
                
        