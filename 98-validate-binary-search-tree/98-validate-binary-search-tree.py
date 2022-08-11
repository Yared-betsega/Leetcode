# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, node, left , right):
        if node:
            if not left < node.val < right:
                return False
                
            checkLeft = self.check(node.left, left,  node.val)
            checkRight = self.check(node.right, node.val, right)
            return checkLeft and checkRight
        return True
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, -float("inf"), float("inf"))