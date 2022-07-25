class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) -1
        m = (l + r) // 2
        best = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                best= mid = m
                break
            if nums[l] <= target and nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        ans = [-1, -1]
        if best != -1:
            ans = [mid, mid]
            l = 0
            r = mid - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    best = m
                if nums[l] <= target and nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = r-1
            ans[0] = best
            
            l = mid + 1
            r = len(nums) - 1
            best = mid
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    best = m
                if nums[l] <= target and nums[m] > target:
                    r = m - 1
                elif nums[m]  < target:
                    l = m + 1
                else:
                    l = l+1
            ans[1] = best
        return ans
            

                