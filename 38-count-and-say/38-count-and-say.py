class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
             return "1"
        num = self.countAndSay(n-1)
        curChar, curAnswer = 0, ""
        for i in range(len(num)):
            if num[i] != num[curChar]:
                curAnswer += str(i-curChar) + str(num[curChar])
                curChar = i
            if i == len(num) - 1:
                curAnswer += str(i-curChar+1) + str(num[curChar])
                curChar = i
        return curAnswer  