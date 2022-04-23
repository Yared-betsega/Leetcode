# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftPrefixProduct = {0:1}
        rightPrefixProduct = {len(nums)-1: 1}
        l, r = 1, len(nums) - 2
        while l < len(nums):
            leftPrefixProduct[l] = leftPrefixProduct[l-1] * nums[l-1]
            rightPrefixProduct[r] = rightPrefixProduct[r+1] * nums[r+1]
            l += 1
            r -= 1
        ans = []
        for i in range(len(nums)):
            ans.append(leftPrefixProduct[i] * rightPrefixProduct[i])
        
        return ans

# time and space complexity 
# time complexity = O(n)
# space complexity = O(n)
            
