# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        queue.append(root)
        answer = []
        
        while queue:
            total = 0
            for temp in queue:
                total += temp.val
            answer.append(total/len(queue))
            
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return answer

# time and space compelxity
# time complexity = O(n)
# space complexity = O(1)