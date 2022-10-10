# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0, None
            
            left, leftChild = dfs(node.left)
            right, rightChild = dfs(node.right)
            if node.val == leftChild == rightChild:
                self.ans = max(self.ans, left + right + 2)
                return max(left, right) + 1, node.val
            if node.val == leftChild:
                self.ans = max(self.ans, left + 1)
                return left + 1, node.val
            if node.val == rightChild:
                self.ans = max(self.ans, right + 1)
                return right + 1, node.val
            self.ans = max(self.ans, left, right)
            return 0, node.val
        dfs(root)
        return self.ans