# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = []
        def dfs(node):
            if node:
                parents.append(node)
                if node.val == target.val:
                    return True
                if dfs(node.left):
                    return True
                if dfs(node.right):
                    return True
                parents.pop()
        dfs(root)
        visited = set()
        def bfs(node, target):
            queue = deque([[node, 0]])
            while queue:
                node, tillNow = queue.popleft()
                if tillNow == target:
                    ans.append(node.val)
                if node.left and node.left.val not in visited:
                    queue.append([node.left, tillNow + 1])
                if node.right and node.right.val not in visited:
                    queue.append([node.right, tillNow + 1])
                
                
        ans = []
        for i in range(len(parents) - 1, -1, -1):
            bfs(parents[i], k)
            k -= 1
            visited.add(parents[i].val)
        return ans
        