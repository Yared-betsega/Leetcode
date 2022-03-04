# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.maxim = 0
        self.cnt = 0
        def dfs(node):
            if node:
                self.cnt += 1
                self.maxim = max(self.maxim, self.cnt)
                dfs(node.left)
                dfs(node.right)
                self.cnt -= 1
            
        def findDeepest(node):
            if node:
                self.cnt += 1
                if self.cnt == self.maxim:
                    self.cnt -= 1
                    return node
                left = findDeepest(node.left)
                right = findDeepest(node.right)
                self.cnt -= 1
                if left and right:
                    return node
                elif left:
                    return left
                elif right:
                    return right
                else:
                    return None
            else:
                return None
            
        dfs(root)
        self.cnt = 0
        return findDeepest(root)
        
        
                
