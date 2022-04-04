# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node, length = head, 0
        while node:
            length += 1
            node = node.next
        
        left = right = None
        node, i = head, 1
        while node:
            if i == k:
                left = node
            if i == length - k + 1:
                right = node
            
            if left and right:
                break
            i += 1
            node = node.next
        
        left.val, right.val = right.val, left.val
        return head

# time and space complexity
# time complexity = O(n)
# space complexity = O(1)
