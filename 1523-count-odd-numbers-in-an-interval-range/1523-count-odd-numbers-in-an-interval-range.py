class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        if low % 2 == 1:
            low += 1
            ans += 1
        if high % 2 == 1:
            high -= 1
            ans += 1
        
        return (high - low) // 2 + ans