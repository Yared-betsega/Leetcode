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
        # Space O(n) solution
#         def preOrder(node, repo):
#             if node:
#                 repo.append(node)
#                 preOrder(node.left, repo)
#                 preOrder(node.right, repo)
        
#         repo = []
#         preOrder(root, repo)
#         i = 0
#         while i < len(repo) - 1:
#             repo[i].left = None
#             repo[i].right = repo[i+1]
#             i += 1
#         return root

# time and space complexity
# time: O(n)
# space: O(n)

        # Space O(1) solution
        node = root
        while node:
            if node.left:
                current = node.left
                while current.right:
                    current = current.right
                current.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
        
        return root

# time and space complexity
# time: O(n)
# space: O(1)
                    