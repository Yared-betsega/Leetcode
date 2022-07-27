"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def construct(node):
            while node:
                if node.child:
                    child = node.child
                    while child.next:
                        child = child.next
                    child.next = node.next
                    node.next = child
                    node = child
            
        node = head
        while node:
            if node.child:
                child = node.child
                while child.next:
                    child = child.next
                child.next = node.next
                if node.next:
                    node.next.prev = child
                node.next = node.child
                node.next.prev = node
                node.child = None
            node = node.next
        return head