# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preOrder(node, repo):
            if node:
                repo.append(node)
                preOrder(node.left, repo)
                preOrder(node.right, repo)
        
        repo = []
        preOrder(root, repo)
        i = 0
        while i < len(repo) - 1:
            repo[i].left = None
            repo[i].right = repo[i+1]
            i += 1
        return root

# time and space complexity
# time: O(n)
# space: O(n)