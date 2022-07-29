class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
             return "1"
        num = self.countAndSay(n-1)
        cur = 0
        ans = ""
        for i in range(len(num)):
            if num[i] != num[cur]:
                ans += str(i-cur)
                ans += str(num[cur])
                cur = i
            if i == len(num) - 1:
                ans += str(i-cur+1)
                ans += str(num[cur])
                cur = i
        return ans            