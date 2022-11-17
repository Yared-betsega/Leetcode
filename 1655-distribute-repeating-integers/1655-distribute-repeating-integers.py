class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        count = Counter(nums)
        count = list(count.values())
        satisfyAll = (1 << len(quantity)) - 1
        
        @lru_cache(None)
        def dp(i, recieved, used):
            if recieved == satisfyAll:
                return True
            if i == len(count):
                return False
            dontUse = dp(i + 1, recieved, 0)
            if dontUse:
                return True
            for q in range(len(quantity)):
                if not recieved & (1 << q):
                    if quantity[q] <= count[i] - used:
                        if dp(i, recieved | (1 << q), used + quantity[q]):
                            return True
            return False
        
        return dp(0, 0, 0)
                
        