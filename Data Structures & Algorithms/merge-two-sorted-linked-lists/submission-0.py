# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Cover edge cases
        # One empty list
        if list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return list1
        
        # Normal execution
        # Create a result linked list and a pointer linked list
        pointer = ListNode()
        res = pointer

        # If neither lists are empty loop
        while list1 and list2:
            # Pointer to the smallest value and move to next
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next

        if list1:
            pointer.next = list1
        else:
            pointer.next = list2
        
        return res.next
