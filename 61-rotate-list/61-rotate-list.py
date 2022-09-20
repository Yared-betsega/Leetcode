# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        if k == 0:
            return head
        count, node = 0, head
        while node:
            count += 1
            node = node.next
        k %= count
        c, node = 0, head
        front = futureHead = ListNode()
        while node:
            if c >= count - k:
                print(node.val)
                front.next = node
                front = front.next
            c += 1
            prev = None
            if c == count - k:
                prev = node
            node = node.next
            if prev:
                prev.next = None
        
        front.next = head
        return futureHead.next