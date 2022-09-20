""" Given the head of a singly linked list, return true if it is a palindrome or false otherwise. """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # make into an array and use two pointers
        nums = []
        current = head
        
        # fill nums array with values
        while current:
            nums.append(current.val)
            current = current.next
            
        l, r = 0, len(nums) - 1
        
        # check l and r values in nums, if ever not equal it's not palindrome
        while l <= r:
            if nums[l] != nums[r]:
                return False
            # update pointers
            l += 1
            r -= 1
        return True

    # solution that doesn't use extra space O(1)
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle of the linked list
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the middle
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # check if palindrome using two pointers
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            else:
                left = left.next
                right = right.next
        return True