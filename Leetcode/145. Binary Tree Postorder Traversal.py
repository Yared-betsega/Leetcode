# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def postOrder(node):
            if node:
                postOrder(node.left)
                postOrder(node.right)
                self.answer.append(node.val)
        
        self.answer = []
        postOrder(root)
        return self.answer

# time and space complexity
# time complexity = O(n)
# space complexity = O(n)
