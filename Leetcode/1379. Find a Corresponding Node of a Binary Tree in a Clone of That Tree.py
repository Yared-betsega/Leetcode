# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node):
            if node:
                if node.val == target.val:
                    return node 
                return dfs(node.left) or dfs(node.right)
        return dfs(cloned)

# time = O(n)
# space = O(n) - For recursive call
