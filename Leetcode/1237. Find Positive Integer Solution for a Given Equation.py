"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        left = 1
        right = z
        ans = []
        while left <= z and right >= 1:
            val = customfunction.f(left, right)
            if val == z:
                ans.append([left, right])
                left += 1
            elif val < z:
                left += 1
            else:
                right -= 1
        return ans
    
# space and time complexity
# time complexity = O(n)
# space complexity = O(n)
