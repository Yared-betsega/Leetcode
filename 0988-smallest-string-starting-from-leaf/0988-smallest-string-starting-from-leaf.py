# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        allStrings = []
        def dfs(node, s):
            s += chr(ord("a") + node.val)
            if not node.left and not node.right: 
                allStrings.append(s[::-1])
            if node.left:
                dfs(node.left, s)
            if node.right:
                dfs(node.right, s)
            
        
        dfs(root, "")
        return min(allStrings)