class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAM = defaultdict(set)
        for user, time in logs:
            UAM[user].add(time)
                
        ans = [0] * k
        for user in UAM:
            ans[len(UAM[user]) - 1] += 1
        return ans