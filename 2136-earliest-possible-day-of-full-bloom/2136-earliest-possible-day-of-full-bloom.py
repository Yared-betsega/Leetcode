class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ptime = 0
        ans = 0
        indices = sorted(range(len(plantTime)), key=lambda x: -growTime[x]) 
        for i in indices:
            ptime += plantTime[i]
            ans = max(ans, ptime + growTime[i])
        return ans