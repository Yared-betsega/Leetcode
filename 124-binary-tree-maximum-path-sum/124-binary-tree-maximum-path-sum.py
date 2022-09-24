# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")
        def dfs(node):
            if node:
                left, right = dfs(node.left), dfs(node.right)
                ans = max(left + node.val, right + node.val, node.val)
                self.ans = max(left, right, ans, left + right + node.val, self.ans)
                return ans
            return -float("inf")
        dfs(root)
        return self.ans
