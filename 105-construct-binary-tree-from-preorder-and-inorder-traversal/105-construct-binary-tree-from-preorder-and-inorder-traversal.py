# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preOrder, inOrder):
            if preOrder and inOrder:
                root = TreeNode(preOrder[0])
                ind = inOrder.index(root.val)
                root.left = build(preOrder[1: ind + 1], inOrder[:ind])
                root.right = build(preOrder[1 + ind: ], inOrder[ind + 1: ])
                return root
    
        return build(preorder, inorder)