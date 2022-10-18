class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        leftIndex = cStart
        rightIndex = cStart 
        bottomIndex = rStart
        topIndex = rStart
        answer = []
        isValid = lambda row, col: 0 <= row < rows and 0 <= col < cols
        
        while len(answer) < rows * cols:
            # print(answer)
            for i in range(leftIndex, rightIndex + 1):
                if isValid(topIndex, i):
                    answer.append([topIndex, i])
            rightIndex += 1
            
            for i in range(topIndex, bottomIndex + 1):
                if isValid(i, rightIndex):
                    answer.append([i, rightIndex])
            bottomIndex += 1
            
            for i in range(rightIndex, leftIndex - 1, -1):
                if isValid(bottomIndex, i):
                    answer.append([bottomIndex, i])
            leftIndex -= 1
            
            for i in range(bottomIndex, topIndex - 1, -1):
                if isValid(i, leftIndex):
                    answer.append([i, leftIndex])
            topIndex -= 1
            
        return answer