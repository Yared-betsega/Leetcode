class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid, hours):
            for i in range(len(piles)):
                if hours <= 0:
                    return False
                hours -= ceil(piles[i] / mid)
            return True if hours >= 0 else False
                
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if check(mid, h):
                r = mid
            else:
                l = mid + 1
        
        return r
        