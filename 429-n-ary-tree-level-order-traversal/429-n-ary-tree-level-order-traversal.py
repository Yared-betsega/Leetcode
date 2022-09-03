"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                for node in cur.children:
                    queue.append(node)
            
            if level:
                ans.append(level)
        
        return ans