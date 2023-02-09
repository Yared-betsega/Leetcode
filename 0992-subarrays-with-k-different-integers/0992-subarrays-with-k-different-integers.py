class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def findAtMostK(k):
            left = ans = 0
            count = Counter()

            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    k -= 1

                count[nums[right]] += 1

                while k < 0:
                    count[nums[left]] -= 1

                    if count[nums[left]] == 0:
                        k += 1

                    left += 1

                ans += right - left + 1

            return ans

        return findAtMostK(k) - findAtMostK(k - 1)