# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        allNumbers = []
        def dfs(node, s):
            s += str(node.val)
            if not node.left and not node.right: 
                allNumbers.append(int(s))
            if node.left:
                dfs(node.left, s)
            if node.right:
                dfs(node.right, s)
            
        
        dfs(root, "")
        return sum(allNumbers)