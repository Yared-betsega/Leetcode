# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node:
                if node.val != self.univalue:
                    return False
                return dfs(node.left) and dfs(node.right)
            
            return True
                
        
        self.univalue = root.val
        return dfs(root)

# time and space complexity 
# time complexity = O(n)
# space complexity = O(n)
