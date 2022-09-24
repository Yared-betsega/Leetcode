# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parents = []
        def collectParents(node):
            parents.append(node)
            if node.val == startValue:
                return True
            
            if node.left and collectParents(node.left):
                return True
            
            if node.right and collectParents(node.right):
                return True
            
            parents.pop()
            return False
        
        ans = []
        def findPath(node, side = None, dontGo = 0):
            if node.val != dontGo:
                if side:
                    ans.append(side)
                if node.val == destValue:
                    return True

                if node.left and findPath(node.left, "L"):
                    return True

                if node.right and findPath(node.right, "R"):
                    return True
                if side:
                    ans.pop()
                return False
            
        collectParents(root)
        # print([p.val for p in parents])
        prevParent = 0
        for parent in reversed(parents):
            
            found = findPath(parent, dontGo = prevParent)
            if found:
                break
            prevParent = parent.val
            ans.append("U")
        return "".join(ans)