# https://leetcode.com/problems/deepest-leaves-sum/

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        tot = 0
        queue = deque([root])
        while queue:
            tot = 0
            for i in range(len(queue)):
                cur = queue.popleft()
                tot += cur.val
                queue.append(cur.left) if cur.left else None
                queue.append(cur.right) if cur.right else None
                
        return tot

# time = O(n)
# space = O(n)
