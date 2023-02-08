class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        heap = []
        for num in nums:
            heappush(heap, -num)
        
        cur = -heappop(heap)
        rank = 1
        while heap:
            temp = -heappop(heap)
            if temp != cur:
                cur = temp
                rank += 1
            if rank == 3:
                return cur
            
        return max(nums)      
