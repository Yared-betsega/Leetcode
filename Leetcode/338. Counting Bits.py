# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Naive Approach
        ans = []
        for i in range(n+1):
            ans.append(bin(i).count("1"))
        return ans
        
        # Bit Manipulation
        ans = []
        for num in range(n+1):
            counter = 0
            while num:
                counter += num&1
                num = num >> 1
            ans.append(counter)
        return ans
    
        # time complexity = O(nlog(n))
        # space complexity = O(1)
