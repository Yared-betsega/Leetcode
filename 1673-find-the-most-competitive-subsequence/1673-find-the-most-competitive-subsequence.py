class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ans, minIndex = [], 0
        for i in range(len(nums)):  
            j = 0
            while ans and len(ans) + len(nums) - i > k and ans[-1] > nums[i]:
                ans.pop()
                j += 1
            ans.append(nums[i])
                
        return ans[:k]
