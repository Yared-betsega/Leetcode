# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        repo = []
        while head:
            repo.append(head.val)
            head = head.next
        maximum = 0
        n, i = len(repo), 0
        while i < len(repo)/2:
            total = repo[i] + repo[n-1-i]
            if total > maximum:
                maximum = total
            i+=1
        return maximum
