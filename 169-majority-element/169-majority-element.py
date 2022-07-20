class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > len(nums)/2:
                return num
            
        # count = Counter(nums)
        # maxim = -1
        # for elem in count:
        #     if count[elem] > len(nums)/2:
        #         return elem
            