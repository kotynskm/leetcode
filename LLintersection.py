""" Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 

If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1: """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# this solution uses O(n) space
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # make a hash set from list A
        hash_first = {}
        curr_first = headA
        curr_second = headB
        
        while curr_first:
            if curr_first not in hash_first:
                hash_first[curr_first] = True
            curr_first = curr_first.next
        
        while curr_second:
            if curr_second in hash_first:
                return curr_second
            else:
                curr_second = curr_second.next
                
        return None

