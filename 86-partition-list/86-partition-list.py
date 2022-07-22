# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        lessThan, moreThan = [], []
        node = head
        while node:
            if node.val < x:
                lessThan.append(node)
            else:
                moreThan.append(node)
            node = node.next
        lessThan.extend(moreThan)
        for i in range(len(lessThan)-1):
            lessThan[i].next = lessThan[i+1]
        lessThan[-1].next = None
        return  lessThan[0]
        