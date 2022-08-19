""" Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node. """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use a fast and slow pointer
        slow, fast = head, head
        
        # loop while fast is not none
        while fast and fast.next:
            # increment slow by 1, and fast by 2
            slow = slow.next
            fast = fast.next.next
        # slow pointer will be sitting on the middle, or second middle node    
        return slow
        