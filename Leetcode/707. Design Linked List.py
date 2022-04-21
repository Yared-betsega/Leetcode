# https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        val, node = 0, self.head
        while node:
            if val == index:
                return node.val
            node = node.next
            val += 1
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, None)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, None)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(val, None)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        i, added = 0, False
        node, prev  = self.head, None
        while node:
            if i == index:
                toBeAdded = Node(val, node)
                prev.next = toBeAdded
                added = True
                break
            i+=1
            prev, node = node, node.next
        if not added and i == index:
            prev.next = Node(val, None)

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next if self.head else None
        else:
            i = 0
            node, prev = self.head, None
            while node:
                if i == index:
                    prev.next = node.next
                i+=1
                prev = node
                node = node.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
