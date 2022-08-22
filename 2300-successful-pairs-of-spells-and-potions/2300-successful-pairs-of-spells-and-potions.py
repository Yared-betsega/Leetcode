class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort(reverse = True)
        ans = []
        for i in range(len(spells)):
            left, right = 0, len(potions) - 1
            best = 0
            while left <= right:
                mid = (left + right) // 2
                if spells[i] * potions[mid] >= success:
                    best = mid + 1
                    left = mid + 1
                else:
                    right = mid - 1
            
            ans.append(best)
        
        return ans
                    