# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    node.left = dfs(node.left)
                    node.right = dfs(node.right)
                    return node
                else:
                    if node.val < low:
                        return dfs(node.right)
                    elif node.val > high:
                        return dfs(node.left) 
        return dfs(root)
                