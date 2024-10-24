# Definition for singly-linked list.
from itertools import filterfalse

from pandas import notnull


class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


     def append (self, value):
         if self.val is None and self.next is None:
             self.val = value
             return
         new = ListNode(val=value)
         current = self
         while current != None:
             if current.next == None:
                 current.next = new
                 break
             current = current.next

     def print_link(self):
         current = self
         while current:
             print(current.val)
             current = current.next

     def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool

        lis = []
        current = head
        while current is not None:
            lis.append(current.val)
            current = current.next

        list2 = lis[::-1]
        print(list2)
        for i in range(len(lis)):
            if list2[i] != lis[i]:
                return False

        return True
        """
        fast_pointer = slow_pointer = head

        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        curr = slow_pointer
        prev = None
        while curr:
            second = curr.next
            curr.next = prev
            prev = curr
            curr = second

        current = head
        current2 = prev
        while current2:
            if current.val != current2.val:
                return False

            current = current.next
            current2 = current2.next

        return True







new = ListNode(1)
new.append(2)
new.append(2)
new.append(1)
new.print_link()
print(new.isPalindrome(new))

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        lis = []
        current = head
        while current is not None:
            lis.append(current.val)
            current = current.next

        list2 = lis.reverse()
        for i in range(len(lis)):
            if list2[i] != lis[i]:
                return False

        return True
