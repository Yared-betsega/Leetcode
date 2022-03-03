# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        turn = 0
        answer = []
        
        if root:
            while queue:
                level = []
                if turn % 2 == 0:
                    for i in range(len(queue)):
                        level.append(queue[i].val)
                else:
                    for i in range(len(queue)-1, -1, -1):
                        level.append(queue[i].val)

                answer.append(level)
                turn += 1

                for i in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
        return answer

# time and space complexity 
# time complexity = O(n)
# space complexity = O(n)
