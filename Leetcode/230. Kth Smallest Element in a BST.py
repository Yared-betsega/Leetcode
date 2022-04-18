# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # In order traversal solution
        self.smallest = []
        self.kthsmallest = 0
        def dfs(node):
            if node:
                dfs(node.left)
                if (not node.left or not node.right) or len(self.smallest) > 0:
                    self.smallest.append(node.val)
                
                if len(self.smallest) == k:
                    self.kthsmallest = self.smallest[-1]
                
                dfs(node.right)
                
        dfs(root)
        return self.kthsmallest

# time and space complexity
# time complexity = O(n)
# space complexity = O(n)
                
