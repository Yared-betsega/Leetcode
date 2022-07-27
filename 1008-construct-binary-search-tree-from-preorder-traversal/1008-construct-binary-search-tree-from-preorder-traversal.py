# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Solution using monotonic stack
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            if preorder[i] < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and preorder[i] > stack[-1].val:
                    temp = stack.pop()
                temp.right = node
            
            stack.append(node)
        
        return root
            
# time and space complexity
# time: O(n)
# space: O(n)