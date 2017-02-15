class Node(object):
    def __init__(self, val):
        self.value = val
        self.next = none

class SLL(object):
    def __init__(self):
        self.head = none

    def printSLL():
        while node:
            print node.val
            node = node.next

    def addBack(val):
        self.tail.next = new Node(val)
        self.tail.next = none
        return self

    def addFront(val):
        if !self.head:
            self.head = new Node(val)
            return self
        node = new Node(val)
        node.next = self.head
        self.head = node
        return self

    def insertBefore(nextVal, val):

    def insertAfter(preVal, val):

    def removeNode(val):
        while val != node.val
            node = node.next
        node.next = node.next.next

    def ReverseList():
        

    def length():
        count = 0
        node = self.head
        while (node):
            count += 1
            node = node.next
        return count

    def max():
        node = self.head
        max = node.val
        while node:
            if node.val > max:
                max = node.val
            node = node.next
        return max

    def average():
        total = 0
        node = self.head
        while node:
            total += node.val
            node = node.next
        avg = total / self.length()
        return avg
