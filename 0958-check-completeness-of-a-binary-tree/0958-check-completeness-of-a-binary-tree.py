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

            queue = []
            queue.append(root)
            is_non_full_node = False

            while len(queue) > 0:
                current_node = queue.pop(0)

                if current_node.left is not None:
                    if is_non_full_node:
                        return False
                    queue.append(current_node.left)
                else:
                    is_non_full_node = True

                if current_node.right is not None:
                    if is_non_full_node:
                        return False
                    queue.append(current_node.right)
                else:
                    is_non_full_node = True

            return True
        
        return is_complete_binary_tree(root)