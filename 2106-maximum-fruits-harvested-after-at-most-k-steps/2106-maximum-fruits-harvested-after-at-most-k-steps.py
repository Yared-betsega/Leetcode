class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        amount = defaultdict(lambda: 0)
        for pos, am in fruits:
            amount[pos] = am

        pre = [0] * (fruits[-1][0] + 1)
        for i in range(fruits[0][0], len(pre)):
            pre[i] = pre[i - 1] + amount[i]
        # print(pre)
        
        ans = 0
        for i in range(startPos, min(startPos + k, fruits[-1][0]) + 1):
            movesLeft = k - (i - startPos)
            leftEnd = min(i - movesLeft, startPos)
            leftEnd = max(leftEnd, 0)
            ans = max(ans, pre[i] - pre[leftEnd] + amount[leftEnd])
            
        for i in range(max(startPos - k, 0), min(startPos, fruits[-1][0]) + 1):
            movesLeft = k - (startPos - i)
            rightEnd = max(i + movesLeft, startPos)
            rightEnd = min(rightEnd, fruits[-1][0])
            ans = max(ans, pre[rightEnd] - pre[i] + amount[i])

        return ans