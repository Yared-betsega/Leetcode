class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num
        lst = list(str(num))
        for i in range(len(lst)):
            for j in range(i,len(lst)):
                lst[i], lst[j] = lst[j], lst[i]
                res = ''.join(lst)
                ans = max(ans, int(res))
                lst[i], lst[j] = lst[j], lst[i]
        return ans