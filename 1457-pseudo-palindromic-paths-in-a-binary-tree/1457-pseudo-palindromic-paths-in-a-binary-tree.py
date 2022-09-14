# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def checkPalindrome(count):
            c = 0
            for i in count:
                if count[i] %2 != 0:
                    c += 1
                if c > 1:
                    return False
            return True
        
        path = []
        count = defaultdict(int)
        self.ans = 0
        def dfs(node):
            path.append(node.val)
            count[node.val] += 1
            if not node.left and not node.right:
                if checkPalindrome(count):
                    self.ans += 1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            
            count[path.pop()] -= 1
        dfs(root)
        return self.ans