# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        height = 0
        node = root
        while node.left:
            node = node.left
            height += 1
        
        def leafExists(mid, node):
            l, r = 0, 2 ** height - 1
            for _ in range(height):
                m = l + (r - l) // 2
                if mid <= m:
                    node = node.left
                    r = m
                else:
                    node = node.right
                    l = m + 1
            return node is not None
        
        left, right = 1, 2 ** height - 1
        while left <= right:
            mid = left + (right - left) // 2
            if leafExists(mid, root):
                left = mid + 1
            else:
                right = mid - 1
        
        return (2 ** height - 1) + left
        
        
        