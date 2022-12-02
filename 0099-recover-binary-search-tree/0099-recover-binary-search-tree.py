# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """    
        def check(node, left , right):
            if node:
                if not left.val < node.val < right.val: 
                    if not left.val < node.val:
                        node.val, left.val = left.val, node.val
                    else:
                        node.val, right.val = right.val, node.val
                    # print(root)
                    check(root, rootLeft, rootRight)

                check(node.left, left,  node)
                check(node.right, node, right)
        
        rootLeft = TreeNode(-float("inf"))
        rootRight = TreeNode(float("inf"))
        check(root, rootLeft, rootRight)
    
# time and space complexity 
# time complexity = O(n)
# space complexity = O(1), if we don't consider the space for the recursion stack
    
        