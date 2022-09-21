class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        l = r = 0
        divs = 0
        pairs = []
        for i in range(len(nums)):
            divs = 0
            for j in range(i, len(nums)):
                if not nums[j] % p:
                    divs += 1
                if divs > k:
                    break
                pairs.append((i, j + 1))
        subs = set()
        ans = 0
        for i, j in pairs:
            subarray = tuple(nums[i: j])
            if subarray not in subs:
                ans += 1
                subs.add(subarray)
        return ans