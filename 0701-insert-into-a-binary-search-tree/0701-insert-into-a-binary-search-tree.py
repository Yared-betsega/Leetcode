# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node, prev):
            if not node:
                if val > prev.val: prev.right = TreeNode(val)
                else: prev.left = TreeNode(val)
                return True
            if node.val > val:
                if insert(node.left, node):
                    return True
            else: 
                if insert(node.right, node):
                    return True
            return False
        if not root:
            return TreeNode(val)
        insert(root, None)
        return root
            
                