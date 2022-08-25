# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = []
        def dfs(node):
            parents.append(node)
            if node.val == start:
                return True
            found = False
            if node.left:
                found = found or dfs(node.left)
            if node.right:
                found = found or dfs(node.right)
            if found:
                return True
            parents.pop()
            return False
        def count(node):
            if not node or node.val in visited:
                return 0
            return 1 + max(count(node.left), count(node.right))
        
        dfs(root)
        visited = set()
        dis = maxLen = 0
        for parent in parents[::-1]:
            maxLen = max(dis + count(parent), maxLen)
            visited.add(parent.val)
            dis += 1
            
        return maxLen - 1
            
            
            
            
            
            
            