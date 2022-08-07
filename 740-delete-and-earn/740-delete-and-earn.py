class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        m = max(nums)
        @cache
        def choose(num):
            if num > m:
                return 0
            if num not in count:
                count[num] = 0
            ans = max(choose(num + 1), num * count[num] + choose(num + 2))
            return ans
        
        return choose(1)
            
            
            