class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        ans = [""]*len(s)
        for i in s:
            index = int(i[-1])-1
            ans[index] = i[:len(i)-1]
        return" ".join(ans)