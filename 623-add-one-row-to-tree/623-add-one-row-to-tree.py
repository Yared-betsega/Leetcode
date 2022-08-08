# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        queue = deque([(root, 1)])
        while queue:
            cur, currentDepth = queue.popleft()
            if currentDepth + 1 == depth:
                left = TreeNode(val, cur.left, None)
                right = TreeNode(val, None, cur.right)
                cur.left = left
                cur.right = right
            else:
                if cur.left:
                    queue.append((cur.left, currentDepth + 1))
                if cur.right:
                    queue.append((cur.right, currentDepth + 1))
        return root
            