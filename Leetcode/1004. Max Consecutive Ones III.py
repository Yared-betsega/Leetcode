class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        fast = slow = 0
        zeros = 0
        maxim = 0
        while fast < len(nums):
            
            if nums[fast] == 0:
                zeros += 1
                
            if zeros == k+1:
                if fast - slow > maxim:
                    maxim = fast - slow
                while nums[slow] == 1:
                    slow += 1
                slow += 1
                zeros -= 1
                
            if fast - slow + 1 > maxim:
                maxim = fast - slow+1
            fast += 1 
            
        return maxim
    
#time space complexity
#time complexity  O(n)
#space complexity O(1)
