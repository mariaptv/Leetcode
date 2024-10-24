class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, value):
        if self is None:
            self.val = value

        new = ListNode(val=value)
        current= self
        while current.next:
            current = current.next

        current.next = new

    def print_lin(self):
        current = self
        while current:
            print(current.val)
            current = current.next

new = ListNode(1)
new.append(2)
new.append(3)
new.append(4)
new.append(5)
new.print_lin()