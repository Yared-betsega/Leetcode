class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            for i in range(left, mid + 1):
                if nums[i] == target:
                    return True
                else:
                    left = mid + 1
        return False

# time and space complexity
# time complexity = O(nlog(n))
# space complexity = O(1)
