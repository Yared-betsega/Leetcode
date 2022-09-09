class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ans = []
        n = len(target)
        curPos = [0, 0]
        for i in range(n):
            ordDif = ord(target[i]) - ord("a")
            verPos = ordDif // 5
            horPos = ordDif - ((verPos) * 5)
            
            verMove = []
            if curPos[0] > verPos:
                verMove = ["U"] * (curPos[0] - verPos)
            elif curPos[0] < verPos:
                verMove = ["D"] * (verPos - curPos[0])
                
            horMove = [] 
            if curPos[1] < horPos:
                horMove = ["R"] * (horPos - curPos[1])
            elif curPos[1] > horPos:
                horMove = ["L"] * (curPos[1] - horPos)
            
            if verPos < 5:
                ans.extend(verMove + horMove)
            else:
                ans.extend(horMove + verMove)
            
            ans.append("!")
            curPos = [verPos, horPos]
            
        return "".join(ans)

# time and space complexity
# time: O(n)
# space: O(n)
                