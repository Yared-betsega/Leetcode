# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def is_complete_binary_tree(root):
            if root is None:
                return True

            queue = deque([root])
            is_non_full_node = False

            while queue:
                current_node = queue.popleft()

                if current_node.left:
                    if is_non_full_node:
                        return False
                    queue.append(current_node.left)
                else:
                    is_non_full_node = True

                if current_node.right:
                    if is_non_full_node:
                        return False
                    queue.append(current_node.right)
                else:
                    is_non_full_node = True

            return True
        
        return is_complete_binary_tree(root)