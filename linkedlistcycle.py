""" Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by

continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false. """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# solution is O(n) time and O(n) space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: 
        # hash set of visited nodes
        visited = {}
        
        # set current node to the head of the list
        current = head
        
        # loop while we have nodes to visit
        while current:
            # if node is not in the visited list, add it
            if current not in visited:
                visited[current] = True
                # update current pointer
                current = current.next
            # otherwise, node must already be in the list meaning we have a cycle
            else:
                return True
            
        return False

# solution with fast and slow pointer O(n) time O(1) space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # set a fast and slow pointer
        slow, fast = head, head
        
        # while fast is not null
        while fast and fast.next:
            # increment the pointers
            slow = slow.next
            fast = fast.next.next
            
            # if slow ever equals fast then we have a cycle
            if slow == fast:
                return True
            
        return False
        