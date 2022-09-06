# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def remove(node):
            if node:
                left, right = remove(node.left), remove(node.right)
                if not left and not right:
                    node.left = node.right = None
                    return True if node.val == 1 else False
                elif not left:
                    node.left = None
                    return True
                elif not right:
                    node.right = None
                    return True
                else:
                    return True
                
        remove(root)
        if not root.left and not root.right and root.val == 0:
            return 
        return root