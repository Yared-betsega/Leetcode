# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        repo = []
        for linkedList in lists:
            node = linkedList
            while node:
                hq.heappush(repo, node.val)
                node = node.next
        
        head = ListNode(0)
        node = head
        while repo:
            val = hq.heappop(repo)
            newNode = ListNode(val)
            node.next = newNode
            node = newNode
        head = head.next
        return head
    
#     space time complexity
#     time complexity = O(nlog(n))
#     space complexity = O(n)
