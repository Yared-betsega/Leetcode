# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        answer = ''
        for i in range(len(s)):
            if s[i] == "]":
                temp = []
                while stack and stack[-1] != "[":
                    temp.append(stack.pop())
                stack.pop()
                mult = ''
                while stack and stack[-1].isdigit():
                    mult += stack.pop()
                stack.append("".join(temp[::-1]) * int(mult[::-1])) 
            else:
                stack.append(s[i])
        
        return ''.join(stack)

# time = O(n)
# space = O(n)
