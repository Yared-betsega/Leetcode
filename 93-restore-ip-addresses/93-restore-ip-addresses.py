class Solution(object):
    def restoreIpAddresses(self, s):
    
        def backtrack(s, i, path, res):
            if i > 4:
                return 
            if i == 4 and not s:
                res.append(path[:-1])
                return 
            for j in range(1, len(s)+1):
                if s[:j]=='0' or (s[0]!='0' and 0 < int(s[:j]) < 256):
                    backtrack(s[j:], i+1, path+s[:j]+".", res)
        res = []
        backtrack(s, 0, "", res)
        return res