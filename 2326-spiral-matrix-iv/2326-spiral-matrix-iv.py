# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        leftIndex = 0
        rightIndex = n - 1
        bottomIndex = m - 1
        topIndex = 0
        currentNode = head
        matrix = [[0 for i in range(n)] for i in range(m)]
        
        while topIndex <= bottomIndex and leftIndex <= rightIndex:
            for i in range(leftIndex, rightIndex + 1):
                matrix[topIndex][i] = currentNode.val if currentNode else -1
                currentNode = currentNode.next if currentNode else None
            topIndex += 1
            if topIndex <= bottomIndex:
                for i in range(topIndex, bottomIndex + 1):
                    matrix[i][rightIndex] = currentNode.val if currentNode else -1
                    currentNode = currentNode.next if currentNode else None
                rightIndex -= 1
                if rightIndex >= leftIndex:
                    for i in range(rightIndex, leftIndex - 1, -1):
                        matrix[bottomIndex][i] = currentNode.val if currentNode else -1
                        currentNode = currentNode.next if currentNode else None
                    bottomIndex -= 1
                    if topIndex <= bottomIndex:
                        for i in range(bottomIndex, topIndex - 1, -1):
                            matrix[i][leftIndex] = currentNode.val if currentNode else -1
                            currentNode = currentNode.next if currentNode else None
                        leftIndex += 1

        return matrix