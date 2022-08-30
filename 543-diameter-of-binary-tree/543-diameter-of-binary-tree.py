# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _max = [0]
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            # print(left + right, node.val)
            _max[0] = max(_max[0], left + right)
            return max(left, right) + 1
        
        dfs(root)
        return _max[0]
            
        
#         """
#         1: left = 2, right = 1 = 3
#         2: left = 1, right = 1 = 2
#         4: left = 0, right = 0 = 0
#         """
#         1-2, 2-4, 
#         time: O(n)
#         recursion
#         psedocode:
#         def rec():
#             if node is leaf:
#                 return 1
#             left <= rec(left)
#             rigth <= rec(right)
#             glomax = max(glomax, left + right)
#             return max(left, right)
            
        