from typing import List
import math

class Solution:
    def maxOperations(self, nums, k):
        numOfPairs = 0
        pairs = {}
        for i in nums:
            if i in pairs:
                pairs[i] = pairs[i] + 1
            else:
                pairs[i] = 1

        for n in pairs:
            difference = k - n
            if difference in pairs and pairs[difference] > 0:
                ops = 0
                if n == k // 2:
                    ops = math.floor(pairs[n] // 2)
                else:
                    ops = min(pairs[n], pairs[difference])

                numOfPairs += ops
                pairs[difference] = pairs[difference] - ops
                pairs[n] = pairs[n] - ops

        return numOfPairs
