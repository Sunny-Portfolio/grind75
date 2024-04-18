# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->
1. The merge function takes in two linked list (* not list)
1. Compare each node and iterate to the next one
1. Create a dummy linked list to save the merged list
1. Use a pointer to the dummy linked list to iterate through the dummy linked list

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(n)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(1)
# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
```