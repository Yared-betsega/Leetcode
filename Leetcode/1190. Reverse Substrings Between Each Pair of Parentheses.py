def reverseParentheses(self, s: str) -> str:
        start = -1
        i = 0
        while i < len(s):
            temp = s
            if s[i] == ")":
                s = ""
                start = temp[:i].rfind("(")
                s += temp[:start]
                x = temp[start+1:i]
                s += x[::-1]
                s += temp[i+1:]
                i = 0
            i+=1
            if "(" not in s:
                break
        return s
