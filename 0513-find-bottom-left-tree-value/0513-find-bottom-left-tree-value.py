# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        level  = 0
        queue = deque([root])
        ans = None
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                if i == 0:
                    ans = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            level += 1
        
        return ans.val