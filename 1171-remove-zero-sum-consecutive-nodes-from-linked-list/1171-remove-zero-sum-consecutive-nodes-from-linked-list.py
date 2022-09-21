# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos, node, toBeRemoved = {0: -1}, head, []
        _sum = index = 0
        while node:
            _sum += node.val
            if _sum in pos:
                toBeRemoved.append((pos[_sum] + 1, index))
            pos[_sum], node = index, node.next
            index += 1
        if len(toBeRemoved) == 0:
            return head
        toBeRemoved.sort(key = lambda x: (x[0], -x[1]))
        merged = [toBeRemoved[0]]
        remove = set([i for i in range(toBeRemoved[0][0], toBeRemoved[0][1] + 1)])
        for i in range(1, len(toBeRemoved)):
            if toBeRemoved[i][0] > merged[-1][1]:
                merged.append(toBeRemoved[i])
                for i in range(toBeRemoved[i][0], toBeRemoved[i][1] + 1):
                    remove.add(i)
        prev = start = ListNode()
        node, i = head, 0
        while node:
            if i not in remove:
                prev.next = node
                prev = prev.next
            node = node.next
            i += 1
        prev.next = None
        return start.next

# time and space complexity
# time: O(n)
# space: O(n)