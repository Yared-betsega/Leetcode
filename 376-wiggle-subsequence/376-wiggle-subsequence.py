class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
#         dp = [[1, 0]] * len(nums)
#         for i in range(len(nums)):
#             for j in range(i):
#                 if j == 0:
#                     if nums[i] != nums[j]:
#                         dp[i] = [dp[j][0] + 1, 1 if nums[i] > nums[j] else -1]
#                 elif dp[j][1] == 1:
#                     if nums[i] < nums[j]:
#                         dp[i] = max(dp[i], [dp[j][0] + 1, -1])
#                 else:
#                     if nums[i] > nums[j]:
#                         dp[i] = max(dp[i], [dp[j][0] + 1, 1])
#         return max(dp)[0]
    
# # time and space complexity
# # time: O(n**2)
# # space: O(n)
            
        inc, dec = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc[i] = dec[i - 1] + 1
                dec[i] = dec[i - 1]
            elif nums[i] < nums[i - 1]:
                dec[i] = inc[i - 1] + 1
                inc[i] = inc[i - 1]
            else:
                inc[i] = inc[i - 1]
                dec[i] = dec[i - 1]
        return max(max(inc), max(dec))
        
        
        