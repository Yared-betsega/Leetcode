# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.answer = 0
        path = []
        dic = defaultdict(int)
        dic[targetSum] = 1
        def dfs(node, _sum):
            path.append(node)
            _sum += node.val
            if _sum in dic:
                self.answer += dic[_sum]
            
            dic[_sum + targetSum] += 1
            if node.left:
                dfs(node.left, _sum)
            if node.right:
                dfs(node.right, _sum)
            
            dic[_sum + targetSum] -= 1
            path.pop()
            
        if not root:
            return 0
        
        dfs(root, 0)
        return self.answer