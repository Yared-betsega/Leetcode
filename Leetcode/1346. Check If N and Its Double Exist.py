# https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        doubles = set()
        for i in range(len(arr)):
            if arr[i] in doubles:
                return True
            
            doubles.add(arr[i]/2)
            doubles.add(2*arr[i])
        
        return False

# time and space complexity
# time complexity = O(n)
# space complexity  = O(n)
