# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def bfs(node):
            if not node:
                return 0
            
            queue = deque([(node, 0)])
            
            while queue:
                cur, length = queue.popleft()
                if not cur.left and not cur.right:
                    return length + 1
                
                if cur.left:
                    queue.append((cur.left, length + 1))
                if cur.right:
                    queue.append((cur.right, length + 1))
        
        return bfs(root)

# time and space complexity 
# time complexity = O(n)
# space complexity = O(n)

                
        
