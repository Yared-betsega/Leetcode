class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = defaultdict(list)
        for i in range(len(strs)):
            zeros = strs[i].count("0")
            count[i] = [zeros, len(strs[i])-zeros]
        
        @cache
        def helper(zeros, ones, cur):
            if zeros < 0 or ones < 0:
                return -float("inf")
            
            if cur == len(strs):
                return 0
            
            return max(helper(zeros, ones, cur+1),1 + helper(zeros - count[cur][0], ones - count[cur][1], cur+1))
        
        return helper(m, n, 0)
            