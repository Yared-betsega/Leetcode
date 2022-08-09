class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arrSet = set(arr)
        dp = [1] * len(arr)
        arr.sort()
        places = {val: i for i, val in enumerate(arr)}
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] / arr[j] in places:
                    dp[i] += dp[j] * dp[places[arr[i] // arr[j]]]
        return sum(dp) % ((10**9)+7)
                