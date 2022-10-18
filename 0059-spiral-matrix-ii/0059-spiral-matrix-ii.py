class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        leftIndex = 0
        rightIndex = n - 1
        bottomIndex = n - 1
        topIndex = 0
        currentNumber = 1
        matrix = [[0 for i in range(n)] for i in range(n)]
        
        while topIndex <= bottomIndex and leftIndex <= rightIndex:
            for i in range(leftIndex, rightIndex + 1):
                matrix[topIndex][i] = currentNumber
                currentNumber += 1
            topIndex += 1
            
            for i in range(topIndex, bottomIndex + 1):
                matrix[i][rightIndex] = currentNumber
                currentNumber += 1
            rightIndex -= 1
            
            for i in range(rightIndex, leftIndex - 1, -1):
                matrix[bottomIndex][i] = currentNumber
                currentNumber += 1
            bottomIndex -= 1
            
            for i in range(bottomIndex, topIndex - 1, -1):
                matrix[i][leftIndex] = currentNumber
                currentNumber += 1
            leftIndex += 1
            
        return matrix