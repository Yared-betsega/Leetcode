class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cr = 0
        for arr in grid:
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < 0:
                    if left == right:
                        print(mid)
                        cr += (len(arr) - mid)
                        break
                    right = mid 
                else:
                    if left == right and arr[-1] < 0:
                        right = mid + 1
                    elif left == right and arr[-1] >= 0:
                        break
                    left = mid + 1
            
        return cr
