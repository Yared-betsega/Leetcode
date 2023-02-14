class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [] 
        num = 1
        for i in range(n):
            if i % 2 == 0:
                ans.append(num)
            else:
                ans.append(-num)
                num += 1
        
        if n % 2:
            ans.pop()
            ans.append(0)
        return ans