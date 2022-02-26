class Solution:
    def helper(self, arr, value):
        total = 0
        for num in arr:
            if num < value:
                total += num
                continue
            total += value
        return total
    
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        left, right = 0, max(arr)
        best = (self.helper(arr, target)-target, right)
        
        while left <= right:
            mid = left + (right - left) // 2
            changed = self.helper(arr, mid)
            difference = abs(changed - target)
            if difference <= best[0]:
                if difference == best[0]:
                    best = (difference, min(best[1], mid))
                else:
                    best = (difference, mid)
            if changed < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return best[1]

# time and space complexity 
# time complexity = O(nlog(m)), m = max(arr) - min(arr)
# space complexity = O(1)
