""" Given the head of a singly linked list, reverse the list, and return the reversed list. """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # set a prev and curr pointer
        prev, curr = None, head
        
        # loop while we have nodes
        while curr:
            # set tmp to curr.next so we can save it
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # prev is our new head so we return it
        return prev