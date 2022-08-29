class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        count = {}
        child = defaultdict(list)
        for i in range(len(parents)):
            child[parents[i]].append(i)
        def dfs(node):
            if not child[node]:
                count[node] = 1
                return 1
            count[node] = 1
            for ch in child[node]:
                count[node] += dfs(ch)
            return count[node]
        dfs(0)
        _max, nuOfHighest = 1, defaultdict(int)
        for i in range(len(parents)):
            score = 1
            for ch in child[i]:
                score *= count[ch]
            if i != 0:
                score *= (count[0] - count[i])
            nuOfHighest[score] += 1
            _max = max(_max, score)
        return nuOfHighest[_max]
            
            