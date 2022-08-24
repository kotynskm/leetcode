""" Given the head of a sorted linked list, delete all duplicates such that each element 

appears only once. Return the linked list sorted as well. """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # set pointer to head
        curr = head
        
        # loop while there are nodes
        while curr and curr.next:
            # compare values, update pointer if match, else update curr to next node
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head