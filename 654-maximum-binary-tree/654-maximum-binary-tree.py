# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lst, l, r):
            if r >= 0 and l<=len(nums)-1 and l <= r:
                if l == r:
                    return TreeNode(nums[l])
                
                mx = l
                for i in range(l, r+1):
                    if nums[mx] < nums[i]:
                        mx = i
                node = TreeNode(nums[mx])
                node.left = build(lst[l:mx], l, mx-1)
                node.right = build(lst[mx+1:r+1], mx+1, r)
                return node
        
        return build(nums, 0, len(nums)-1)

# time and space complexity
# time: O(n)
# space: O(1)