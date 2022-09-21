class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        l = r = 0
        divs = ans = 0
        ans = set()
        for i in range(len(nums)):
            divs = 0
            for j in range(i, len(nums)):
                if not nums[j] % p:
                    divs += 1
                if divs > k:
                    break
                ans.add(tuple(nums[i: j + 1]))
        return len(ans)