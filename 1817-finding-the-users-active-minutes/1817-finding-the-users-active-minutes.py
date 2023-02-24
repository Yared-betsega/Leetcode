class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAM = defaultdict(set)
        for user, time in logs:
            UAM[user].add(time)
        
        count = Counter(map(lambda x: len(x[1]), UAM.items()))
        
        ans = []
        for i in range(k):
            ans.append(count[i + 1])
        return ans