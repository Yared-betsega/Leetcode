
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

class Solution:
    def countOrders(self, n: int) -> int:
        
        def permutation(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                return n * permutation(n-1)
            
        def count(p, d, memo):
            
            if (p, d) in memo:
                return memo[(p, d)]
            
            if p == 0:
                memo[(p, d)] = permutation(d)
                return memo[(p, d)]
            if p == d:
                memo[(p, d)] = p * count(p-1, d, memo)
                return memo[(p, d)]
            else:
                ps = p * count(p-1, d, memo)
                ds = (d-p) * count(p, d-1, memo)
                memo[(p, d)] = ps + ds
                return memo[(p, d)]
        
        return count(n, n, {}) % (10**9 + 7)
    
# dp solution 
# time and space complexity
# time complexity = O(n**2)
# space complexity = O(n**2)
