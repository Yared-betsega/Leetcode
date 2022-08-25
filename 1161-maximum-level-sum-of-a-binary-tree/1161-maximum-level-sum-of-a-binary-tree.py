# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue, level = deque([root]), 1
        max_sum, answer = -float("inf"), 1
        while queue:
            _sum = 0
            for i in range(len(queue)):
                cur = queue.popleft()
                _sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if _sum > max_sum:
                max_sum = _sum
                answer = level
            level += 1
        return answer

# time and space complexity
# time: O(n)
# space: O(n)
                