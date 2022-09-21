class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l <= r:
            if r - l + 1 == k:
                return arr[l:r + 1]
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1
            
        