# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newLinkedList = ListNode()      # Create a singly linked list
        currentNode = newLinkedList     # CurrentNode act as pointer to the new dummy linked list
        while list1 and list2:
            # Compare value of the current iteration of the two lists and add to dummy linked list
            if list1.val < list2.val:
                currentNode.next = list1
                list1 = list1.next
            else:
                currentNode.next = list2
                list2 = list2.next
            currentNode = currentNode.next  # set pointer to next

        # Link the last node if exist (assume only one node left)
        if list1:
            currentNode.next = list1
        elif list2:
            currentNode.next = list2

        # Alternative while loop, but may not be needed

        # while list1 or list2:
        #     if list1:
        #         currentNode.next = list1
        #         list1 = list1.next
        #     else:
        #         currentNode.next = list2
        #         list2 = list2.next
        #     currentNode = currentNode.next

        return newLinkedList.next



def create_linked_list(elements):
    """ Helper function to convert a list to a linked list. """
    dummy = ListNode(0)
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val, end='')
        head = head.next
    print()


# Create linked lists from lists
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([2, 2, 4, 6, 7, 8])

print('Start:')
print_linked_list(list1)
print_linked_list(list2)

newIns = Solution()     # create a new instance of the Solution() class
test = newIns.mergeTwoLists(list1, list2)
print('Results:')
print_linked_list(test)