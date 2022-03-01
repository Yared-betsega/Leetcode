# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.add = 0
        def add(node):
            if node:
                self.add += node.val
                add(node.left)
                add(node.right)
                
        def findDiff(node):
            self.add = 0
            add(node.left)
            left, self.add = self.add, 0
            add(node.right) 
            right, self.add = self.add, 0
            return abs(left - right)
        
        def allTilt(node):
            if node:
                self.total += findDiff(node)
                allTilt(node.left)
                allTilt(node.right)
                
        allTilt(root)
        return self.total
        
