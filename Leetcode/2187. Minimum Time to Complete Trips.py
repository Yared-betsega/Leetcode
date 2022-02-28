class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = min(time), 10**14
        while left < right:
            mid = left + (right - left) // 2
            total = 0
            for i in time:
                total += (mid // i)
            if total < totalTrips:
                left = mid + 1
            else:
                right = mid
        return right

# time and space complexity
# time complexity = O(log(n)), n = 10**14
# space complexity = O(1)
