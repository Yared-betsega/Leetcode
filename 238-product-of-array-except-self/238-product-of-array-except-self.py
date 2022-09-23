class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = nums.count(0)
        if c > 1:
            return [0] * len(nums)
        elif c == 1:
            ans = [0] * len(nums)
            ind = nums.index(0)
            _prod = 1
            for num in nums:
                if num != 0:
                    _prod *= num
            ans[ind] = _prod
            return ans
        else:
            _prod = reduce(lambda x, y: x * y, nums)
            ans = []
            for num in nums:
                ans.append(_prod // num)
            return ans
    

# time and space complexity 
# time complexity = O(n)
# space complexity = O(1)
            