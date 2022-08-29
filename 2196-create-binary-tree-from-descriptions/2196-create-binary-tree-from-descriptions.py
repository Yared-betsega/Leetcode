# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node = {}
        childs = set()
        for par, ch, isleft in descriptions:
            if par not in node:
                node[par] = TreeNode(par)
            if ch not in node:
                node[ch] = TreeNode(ch)
            if isleft:
                node[par].left = node[ch]
            else:
                node[par].right = node[ch]
            childs.add(ch)
        
        for par, ch, isleft in descriptions:
            if par not in childs:
                return node[par]
            