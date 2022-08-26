""" Given the head of a linked list, remove the nth node from the end of the list and return its head. """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow, fast = dummy, dummy
        
        while fast.next:
            # increment the fast pointer until reach n distance between pointers
            fast = fast.next
            n -= 1
            if n < 0:
                slow = slow.next

        # when fast.next becomes None, slow pointer will be pointing to node whose next we need to move
        slow.next = slow.next.next
        
        return dummy.next