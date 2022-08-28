class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        n = min(len(firstList), len(secondList))
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            cur = [firstList[i], secondList[j]]
            cur.sort()
            if cur[0][1] >= cur[1][0]:
                answer.append([max(cur[0][0], cur[1][0]), min(cur[0][1], cur[1][1])])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            elif firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                if firstList[i][0] < secondList[j][0]:
                    i += 1
                else:
                    j += 1
        return answer
            