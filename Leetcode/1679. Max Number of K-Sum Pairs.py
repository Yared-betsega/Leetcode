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
   

# Two pointer solution
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r, ans = 0, len(nums)-1, 0
        while l < r:
            if nums[l] + nums[r] == k:
                ans += 1
                l += 1
                r-= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else: l += 1
        return ans

# time and space complexity
# time complexity = O(nlog(n))
# space complexity = O(1)
                    
            
        
