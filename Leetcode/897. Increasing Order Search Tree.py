# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, repo):
        if not node:
            return
        repo.append(node.val)
        self.helper(node.left, repo)
        self.helper(node.right, repo)
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        repo = []
        self.helper(root, repo)
        repo.sort()
        
        root = TreeNode()
        node = root
        for i in range(len(repo)):
            node.right = TreeNode(repo[i])
            node = node.right
        node.right = None
        
        return root.right
      
# time and space complexity 
# time complexity = O(nlog(n))
# space complexity = O(1)
