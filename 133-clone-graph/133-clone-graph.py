"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        visited = set()
        nodes = defaultdict(lambda: Node())
        def dfs(original):
            nodes[original.val].val = original.val
            visited.add(original.val)
            for nbr in original.neighbors:
                nodes[original.val].neighbors.append(nodes[nbr.val])
                if nbr.val not in visited:
                    dfs(nbr)
        dfs(node)
        return nodes[1]
            