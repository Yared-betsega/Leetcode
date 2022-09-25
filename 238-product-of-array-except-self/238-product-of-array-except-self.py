class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        ans = []
        for i in range(len(nums)):
            ans.append(pre)
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= post
            post *= nums[i]
        
        return ans

# time and space complexity 
# time complexity = O(n)
# space complexity = O(1)
            