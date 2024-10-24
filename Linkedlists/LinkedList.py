
class Linked:

    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        node.prev = current

    def print_link(self):
        current= self.head
        while current:
            print(current.val)
            current = current.next

    def beginning (self, value):
        node = Node(value)
        self.head.prev = node
        node.next= self.head
        self.head = node

    def reverse (self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            current.prev =next
            prev = current
            current = next
        self.head = prev




class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

new = Linked()
new.append(1)
new.append(2)
new.append(3)
new.append(4)
new.beginning(5)
new.print_link()
print("reverse")
new.reverse()
new.print_link()
