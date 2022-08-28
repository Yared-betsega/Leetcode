class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            store = {}
            for j in range(i + 1, len(nums)):
                if nums[j] in store:
                    ans.add((nums[j], store[nums[j]][0], store[nums[j]][1]))
                wanted = -(nums[i] + nums[j])
                store[wanted] = (nums[i], nums[j])
                    
                        
        return ans