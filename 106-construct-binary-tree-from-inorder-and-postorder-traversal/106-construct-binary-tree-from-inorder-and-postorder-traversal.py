# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(inorder, postorder):
            if inorder:
                root = TreeNode(postorder[-1])
                i = inorder.index(root.val)
                root.left = dfs(inorder[:i], postorder[:i])
                root.right = dfs(inorder[i + 1:], postorder[i: len(postorder) - 1])
                return root

        return dfs(inorder, postorder)