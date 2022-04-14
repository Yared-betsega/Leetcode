# https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        all = 2**p - 1
        
        return pow(all-1, all//2, 10**9 + 7) * all % (10**9 + 7)
     
 
# time and space complexity
# time complexity = O(1)
# space complexity = O(1)
