class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new = Node(data)
        current = self.head
        if current == None:
            self.head = new
            return

        while current != None:
            if current.next == None:
                current.next = new
                new.prev = current
                return
            current = current.next

    def print_link (self):
        current = self.head
        while current != None:
            print(current.data)
            current= current.next

    def push(self, value):
        new = Node(value)
        old_head = self.head
        self.head = new
        new.next = old_head



new = LinkedList()
new.add( 9)
new.add( 5)
new.add( 2)
new.add( 1)
new.push(897897)
new.print_link()



