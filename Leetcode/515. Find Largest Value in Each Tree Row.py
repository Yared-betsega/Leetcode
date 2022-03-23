
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        maxList = []
        while queue:
            maxOfRow = -float(inf)
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.val > maxOfRow:
                    maxOfRow = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            maxList.append(maxOfRow)
        
        return maxList
            
# time and space complexity
# time complexity = O(n)
# space complexity = O(n)
