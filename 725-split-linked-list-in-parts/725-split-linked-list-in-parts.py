# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        ans, node = [], head
        if count <= k:
            while node:
                ans.append(node)
                node = node.next
                ans[-1].next = None
            for i in range(k - count):
                ans.append(None)
        else:
            div = count // k
            partition = [div] * k
            count -= div * k
            for i in range(count):
                partition[i] += 1
            for i, val in enumerate(partition):
                ans.append(node)
                prev = node
                for j in range(val):
                    prev = node
                    node = node.next
                prev.next = None    
        return ans

# time and space complexity
# time: O(n)
# space: O(k)