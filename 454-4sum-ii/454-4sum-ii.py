class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        ans, n = 0, len(nums1)
        firstAndSecond = defaultdict(int)
        for i in nums1:
            for j in nums2:
                firstAndSecond[(i + j)] += 1
        for i in nums3:
            for j in nums4:
                if -(i + j) in firstAndSecond:
                    ans += firstAndSecond[-(i + j)]
        return ans

# time and space complexity
# time: O(n ** 2)
# space: O(n)