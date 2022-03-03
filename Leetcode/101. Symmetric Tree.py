# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
            i = 0
            j = len(queue) - 1
            while i <= j:
                if (queue[i].val if queue[i] else None) != (queue[j].val if queue[j] else None):
                    return False
                i += 1
                j -= 1
        return True
    
