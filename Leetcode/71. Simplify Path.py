# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = ["/"]
        for subDir in path:
            if subDir == "..":
                if len(stack) > 1:
                    stack.pop()
            elif subDir != "" and subDir != ".":
                stack.append(subDir + "/")  
                
        answer = "".join(stack)
        return answer[:-1] if len(answer)>1 and answer[-1] == "/" else answer

# time complexity = O(n)
# space complexity = O(n)
