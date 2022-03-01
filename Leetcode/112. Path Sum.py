# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.result = set()
        self.total = 0
        def helper(node):
            if node:
                self.total += node.val
                if not node.left and not node.right:
                    if self.total == targetSum:
                        self.result.add(True)
                helper(node.left)
                helper(node.right)
                self.total -= node.val
                
        helper(root)
        return True if True in self.result else False
