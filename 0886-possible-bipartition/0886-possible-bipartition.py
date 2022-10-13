class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        hates = defaultdict(set)
        for i, j in dislikes:
            hates[i].add(j)
            hates[j].add(i)
        
        def dfs(root):
            for i in hates[root]:
                if color[i] == color[root]:
                    return False
                if color[i] == -1:
                    color[i] = 1 - color[root]
                    if not dfs(i):
                        return False
            return True
        
        color = defaultdict(lambda: -1)
        for i in range(1, n + 1):
            if color[i] == -1:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
            