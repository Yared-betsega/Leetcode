# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node:
                ans = 0
                if node.left:
                    if not node.left.left and not node.left.right:
                        ans += node.left.val
                ans += dfs(node.left) + dfs(node.right)
                return ans
            return 0
        return dfs(root)
        def bfs(node):
            queue = deque([node])
            total = 0
            
            while queue:
                cur = queue.popleft()
                
                if cur.left:
                    if not cur.left.left and not cur.left.right:
                        total += cur.left.val
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
            return total

        return bfs(root)
    
# time and space complexity
# time complexity = O(n)
# space complexity = O(n)