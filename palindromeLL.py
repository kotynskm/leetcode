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