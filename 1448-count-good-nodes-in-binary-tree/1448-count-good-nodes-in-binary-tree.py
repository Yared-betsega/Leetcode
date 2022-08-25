# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = [0]
        def dfs(node, _max):
            if node.val >= _max:
                answer[0] += 1
            if node.left:
                dfs(node.left, max(_max, node.val))
            if node.right:
                dfs(node.right, max(_max, node.val))
        
        dfs(root, -float("inf"))
        return answer[0]

# time and space complexity
# time: O(n)
# space: O(n) considering the recursion stack