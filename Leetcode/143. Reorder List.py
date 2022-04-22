# https://leetcode.com/problems/reorder-list/

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node, repo = head, []
        while node:
            repo.append(node)
            node  = node.next
        head = repo[0]
        node = head
        j, l, r = 1, 1, len(repo) - 1
        
        while l<=r:
            if j % 2 == 0:
                node.next = repo[l]
                l+=1
            else:
                node.next = repo[r]
                r-=1
            node = node.next
            j+=1
        node.next = None

# time and space complexity 
# time complexity = O(n)
# space complexity = O(n)     
