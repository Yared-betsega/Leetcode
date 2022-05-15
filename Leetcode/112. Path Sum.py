# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, total):
            if node:
                total += node.val
                if not node.left and not node.right:
                    if total == targetSum:
                        return  True
                left = helper(node.left, total)
                right = helper(node.right, total)
                return left or right
                
        return helper(root, 0)

# time = O(n)
# space = O(1)
