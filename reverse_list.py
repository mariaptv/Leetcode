

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next




def add(head, value):
    current= head
    while current != None:
        if current.next == None:

            new_node = ListNode(value)
            current.next = new_node
            return
        current = current.next

def print_list( head):
    current = head
    while current != None:
        print(current.val)
        current = current.next
def reverse (head):
    current = head
    prev = None

    while current != None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def insert_head (head, value):

    new = ListNode(value)
    new.next = head
    return new



new = ListNode(5)
add(new, 4)
add(new, 8)
add(new, 9)
add(new, 3)

print_list(new)

#print_list(reverse(new))

head = print_list(insert_head(new, 11))
print_list(head)