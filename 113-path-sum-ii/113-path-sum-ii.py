# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.temp = []
        self.answer = []
        self.total = 0
        def dfs(node):
            if node:
                self.total += node.val
                self.temp.append(node.val)
                if not node.left and not node.right:
                    if self.total == targetSum:
                        self.answer.append(copy.deepcopy(self.temp))
                dfs(node.left)
                dfs(node.right)
                self.total -= node.val
                self.temp.pop()
                
            
        dfs(root)
        return self.answer
                        
            
            