class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dic = {}
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] * nums[j] in dic:
                    ans += dic[nums[i] * nums[j]] * 8
                    dic[nums[i] * nums[j]] += 1
                else:
                    dic[nums[i] * nums[j]] = 1
        return ans
                    
                