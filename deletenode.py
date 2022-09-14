""" There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list. """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # current node
        current_node = node
        
        # reassign given node value to it's next value
        current_node.val = current_node.next.val
        
        # now reassign the nodes pointer to the next next node to delete the duplicate
        current_node.next = current_node.next.next