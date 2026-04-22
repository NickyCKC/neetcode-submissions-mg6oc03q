# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        pointer = head.next
        head.next = None
        
        while pointer != None:
            temp_pointer = pointer.next
            pointer.next = head
            head = pointer
            pointer = temp_pointer
        return head
            
        
