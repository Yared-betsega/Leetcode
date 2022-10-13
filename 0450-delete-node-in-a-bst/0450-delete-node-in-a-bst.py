# Definition for a binary tree toBeDel.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        toBeDel, prev = root, None
        while toBeDel and toBeDel.val != key:
            if toBeDel.val < key:
                prev, toBeDel = toBeDel, toBeDel.right
            else:
                prev, toBeDel = toBeDel, toBeDel.left
                
        if not toBeDel:
            return root
        
        if toBeDel.right:
            head = toBeDel.right
            while head.left:
                head = head.left
            head.left = toBeDel.left
        else: toBeDel.right = toBeDel.left
            
        if toBeDel.val == root.val:
            return root.right
        
        if toBeDel.val > prev.val:
            prev.right = toBeDel.right
        else:
            prev.left = toBeDel.right
        return root
        