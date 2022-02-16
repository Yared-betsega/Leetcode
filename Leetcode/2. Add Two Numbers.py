# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        node = head
        rem = 0
        while l1 or l2:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            add = first + second + rem
            temp = ListNode()
            if add >= 10:
                temp.val = add -10
                rem = 1
            else:
                temp.val = add
                rem = 0
            if not head:
                head = temp
                node = head
            else:
                node.next = temp
                node = temp
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if rem != 0:
            temp = ListNode(rem)
            node.next = temp
        return head
