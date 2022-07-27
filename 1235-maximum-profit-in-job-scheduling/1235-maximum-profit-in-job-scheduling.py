class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def binarySearch(i, val):
            if elements[-1][0] < val:
                return -1
            l, r = i, len(elements)-1
            while l < r:
                m = (l + r) // 2
                if elements[m][0] >= val:
                    r = m
                else:
                    l = m + 1
            return r
        
        elements = []
        for i in range(len(startTime)):
            elements.append([startTime[i], endTime[i], profit[i]])
        elements.sort()
        
        dp = [0] * (len(elements)+1)
        for i in range(len(elements)-1, -1, -1):
            start = binarySearch(i, elements[i][1])
            dp[i] = max(dp[i+1], elements[i][2]+dp[start])
        # print(dp)
        # print(elements)
        return dp[0]
        