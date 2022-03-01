"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.cnt = [0]
        self.visited = set()
        self.maxim = 0
        self.cnt = 0
        def helper(node):
            if node and node not in self.visited:
                self.visited.add(node)
                self.cnt += 1
                if self.cnt > self.maxim:
                    self.maxim = self.cnt
                if len(node.children)>0:
                    for i in node.children:
                        helper(i)
                self.cnt -= 1
        helper(root)
        return self.maxim
