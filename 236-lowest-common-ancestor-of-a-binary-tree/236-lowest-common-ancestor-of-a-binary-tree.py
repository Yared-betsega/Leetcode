# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, target, ancestors):
            if node:
                if node.val == target.val:
                    ancestors.append(node.val)
                    return True 
                found = dfs(node.left, target, ancestors)
                if found:
                    ancestors.append(node.val)
                    return True
                found = dfs(node.right, target, ancestors)
                if found:
                    ancestors.append(node.val)
                    return True
                
        p_ancestors = []
        dfs(root, p, p_ancestors) 
        q_ancestors = []
        dfs(root, q, q_ancestors)
        q_ancestors = set(q_ancestors)
        for i in range(len(p_ancestors)):
            if p_ancestors[i] in q_ancestors:
                return TreeNode(p_ancestors[i])

# time and space complexity
# time: O(n)
# space: O(n)
