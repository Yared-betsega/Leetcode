# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def preOrder(node):
            if node:
                self.answer.append(node.val)
                preOrder(node.left)
                preOrder(node.right)
        
        self.answer = []
        preOrder(root)
        return self.answer

# time and space complexity 
# time complexity = O(n)
# space complexity = O(n)
