""" You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list. """


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node for new sorted list
        dummy = ListNode()
        # set current to the dummy node
        current = dummy
        # loop while l1 and l2 have values, compare the values
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                # move the pointer forward
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
                
            # update current pointer
            current = current.next
        
        # if any remaining elements in l1 or l2
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        # dummy.next is the first node of our new sorted list
        return dummy.next