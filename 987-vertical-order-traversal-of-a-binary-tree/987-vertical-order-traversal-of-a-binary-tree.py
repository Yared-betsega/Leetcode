# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        grid = defaultdict(list)
        def traverse(node, row, col):
            grid[(row, col)].append(node.val)
            if node.left:
                traverse(node.left, row + 1, col - 1)
            if node.right:
                traverse(node.right, row + 1, col + 1)
            
        traverse(root, 0, 0)
        matrix = sorted(grid.items(), key = lambda x: (x[0][1], x[0][0]))
      
        cur = matrix[0][0][1]
        ans = []
        for (row, col), nodes in matrix:
            if not ans or cur != col:
                ans.append(sorted(nodes))
                cur = col
            else:
                ans[-1].extend(sorted(nodes))
        return ans