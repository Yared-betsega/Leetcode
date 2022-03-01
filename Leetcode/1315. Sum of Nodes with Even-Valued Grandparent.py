# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        def dfs(node, father, grandpa):
            if node:
                if grandpa and grandpa % 2 == 0:
                    self.total += node.val
                dfs(node.left, node.val, father)
                dfs(node.right, node.val, father)
                
        dfs(root, 1, 1)
        return self.total

# time and space complexity 
# time compelexity = O(n)
# space complexity = O(1)
