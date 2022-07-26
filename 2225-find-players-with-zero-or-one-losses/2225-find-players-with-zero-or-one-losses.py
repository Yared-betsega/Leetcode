class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        indegree = defaultdict(int)
        players = set()
        for match in matches:
            indegree[match[1]] += 1
            players.add(match[0])
            players.add(match[1])
            
        ans = [[], []]
        for i in players:
            if indegree[i] == 0:
                ans[0].append(i)
            if indegree[i] == 1:
                ans[1].append(i)
            
        return [sorted(ans[0]), sorted(ans[1])]

# time and space complexity
# time: O(nlogn)
# space: O(n)