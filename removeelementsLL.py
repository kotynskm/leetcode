""" Given the head of a linked list and an integer val, remove all the nodes of the linked list that 

has Node.val == val, and return the new head.

 """

 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # create dummy node
        dummy = ListNode(next=head)
        # set pointers for prev and current
        prev, curr = dummy, head
        
        # loop while we have nodes
        while curr:
            # check if val is target
            if curr.val == val:
                # if it is target then move prev pointer to curr.next node
                prev.next = curr.next
            else:
                # update prev to curr node
                prev = curr
            
            # update curr
            curr = curr.next
           
        # dummy.next points to head of our list
        return dummy.next