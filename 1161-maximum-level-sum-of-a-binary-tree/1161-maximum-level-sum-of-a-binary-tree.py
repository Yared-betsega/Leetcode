# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        count = defaultdict(list)
        level =  1
        while queue:
            _sum = 0
            for i in range(len(queue)):
                cur = queue.popleft()
                _sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            count[_sum].append(level)
            level += 1
        return min(count[max(count)])

# time and space complexity
# time: O(n)
# space: O(n)
                