class Solution:
    def compress(self, chars: List[str]) -> int:
        fast = 0
        slow = 0
        s = ""
        while fast < len(chars):
            if chars[fast] != chars[slow]:
                length = fast - slow
                s += chars[slow]
                if length > 1:
                    s += str(length)
                slow = fast
            fast += 1
        length = fast - slow
        s += chars[slow]
        if length > 1:
            s += str(length)
        
        chars.clear()
        chars.extend(list(s))
        
        return len(s)
