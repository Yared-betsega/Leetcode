# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = start = ListNode(-200)
        node = head
        while node and node.next:
            if node.val != node.next.val:
                prev = node
                node = node.next
            else:
                while node.next and node.val == node.next.val:
                    node = node.next
                prev.next = node.next
                node = node.next
            if not start.next:
                start.next = prev if start.val != prev.val else None
        return start.next
        # prev = ListNode()
        # node = head
        # head = prev
        # added = set()
        # rep = set()
        # while node:
        #     if node.val in added: 
        #         prev.next = node.next
        #         rep.add(node.val)
        #         node = prev.next
        #     else:
        #         prev.next = node
        #         prev = node
        #         node = node.next
        #         added.add(prev.val)
        # prev = head
        # node = head.next
        # while node:
        #     if node.val in rep:
        #         prev.next = node.next
        #         node = prev.next
        #     else:
        #         prev.next = node
        #         prev = node
        #         node = node.next
        # return head.next