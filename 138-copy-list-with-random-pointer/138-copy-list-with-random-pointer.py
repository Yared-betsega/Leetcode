"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        index = {}
        copy = []
        node, i = head, 0
        while node:
            copy.append(Node(node.val))
            index[node] = i
            node = node.next
            i += 1
        copy.append(None)
        node, i = head, 0
        while node:
            copy[i].next = copy[i + 1]
            if node.random:
                copy[i].random = copy[index[node.random]]
            node = node.next
            i += 1
        return copy[0]
    
# time and space complexity
# time: O(n)
# space: O(n)
            
            