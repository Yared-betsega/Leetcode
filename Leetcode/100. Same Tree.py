# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(node, values):
            
            if node:
                values.append(node.val)
                if node.left:
                    dfs(node.left, values)
                else:
                    values.append(None)
                
                if node.right:
                    dfs(node.right, values)
                else:
                    values.append(None)
                
            return values
        
        first = dfs(p, [])
        second = dfs(q, [])
        
        return first == second
                
