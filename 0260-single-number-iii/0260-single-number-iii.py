class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        carret = reduce(lambda x, y: x ^ y, nums)
        bitDiff = carret & (-carret)
        first = 0
        for num in nums:
            if num & bitDiff:
                first ^= num
                
        return [first, carret ^ first]

# time and space complexity
# time: O(n)
# space: O(1)