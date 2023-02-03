class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for subDir in path:
            if subDir == "..":
                if stack:
                    stack.pop()
            elif subDir != "" and subDir != ".":
                stack.append(subDir)    
        return "/" + "/".join(stack)

# time complexity = O(n)
# space complexity = O(n)