# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         ans = [-float("inf")] * (len(nums)-1)
#         ans.append(nums[-1])
#         dec = deque()
        
#         for i in range(len(nums) - 2, -1, -1):
#             while dec and dec[-1] - i > k:
#                 dec.pop()
#             while dec and ans[i+1] > ans[dec[0]]:
#                 dec.popleft()
#             dec.appendleft(i+1)
            
#             ans[i] = nums[i] + ans[dec[-1]]
            

#         return ans[0]

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dq=deque([(nums[0],0)])
        for i in range(1,len(nums)):
            score=dq[0][0]+nums[i]
            while dq and dq[-1][0]<score: dq.pop()
            dq.append((score,i))
            if dq[0][1]==i-k: dq.popleft()
        return dq[-1][0]