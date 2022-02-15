# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = []
        temp = prev = head
        
        while temp:
            if temp.val not in store:
                store.append(temp.val)
                prev = temp
                temp = temp.next
            else:
                while temp and temp.val in store:
                    prev.next = prev.next.next
                    temp = temp.next
                prev = prev.next
            
        return head
