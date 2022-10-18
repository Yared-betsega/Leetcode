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
        matrix = [[-1 for i in range(n)] for i in range(m)]
        
        while topIndex <= bottomIndex and leftIndex <= rightIndex and currentNode:
            for i in range(leftIndex, rightIndex + 1):
                if currentNode:
                    matrix[topIndex][i] = currentNode.val 
                    currentNode = currentNode.next
                else: break
            topIndex += 1
            if topIndex <= bottomIndex and currentNode:
                for i in range(topIndex, bottomIndex + 1):
                    if currentNode:
                        matrix[i][rightIndex] = currentNode.val 
                        currentNode = currentNode.next
                    else: break
                rightIndex -= 1
                if rightIndex >= leftIndex:
                    for i in range(rightIndex, leftIndex - 1, -1):
                        if currentNode:
                            matrix[bottomIndex][i] = currentNode.val 
                            currentNode = currentNode.next
                        else:
                            break
                    bottomIndex -= 1
                    if topIndex <= bottomIndex:
                        for i in range(bottomIndex, topIndex - 1, -1):
                            if currentNode:
                                matrix[i][leftIndex] = currentNode.val 
                                currentNode = currentNode.next
                            else:
                                break
                        leftIndex += 1

        return matrix