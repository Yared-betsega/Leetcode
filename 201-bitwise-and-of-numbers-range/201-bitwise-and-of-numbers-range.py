class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        
        # To get the shortest lenght of the binary representation of the largest element
        # Takes O(32) ~ O(1) time complexity
        for i in range(32):
            if right & (1 << i):
                maxBinLength = 32 - i
                break
        
        # Add check if each bit index in the above maxBinLength are on or off 
        # if it is on make the corresponding bit index of the answer on
        ans = cur = 0
        for i in range(maxBinLength - 1, -1, -1):
            if right & (1 << i):
                cur += (1 << i)
                if left >= cur:
                    ans += (1 << i)
        return ans

# time and space complexity
# time: O(32)
# space: O(1)
                