#Merge Two Sorted Lists
#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#Return the head of the merged linked list.

# Definition for singly-linked list.
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


def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if list1 == None:
        return list2
    elif list2 == None:
        return list1
    elif list1 == None and list2 == None:
        return []

    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next




new_node = ListNode(1)
add(new_node, 2)
add(new_node, 3)
add(new_node, 4)
add(new_node, 5)

new_node2 = ListNode(1)
add(new_node2, 3)
add(new_node2, 3)
add(new_node2, 4)
add(new_node2, 5)
print_list(mergeTwoLists(new_node2, new_node))