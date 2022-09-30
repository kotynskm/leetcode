""" Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space. """

# solution modifies input array by sorting it O(n log n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # sort the numbers
        sorted_nums = sorted(nums)
        
        # use two pointers to compare numbers, first duplicate number pair is the answer
        l, r = 0, 1
        
        while r < len(nums):
            if sorted_nums[l] == sorted_nums[r]:
                return sorted_nums[l]
            else:
                l += 1
                r += 1

# this is a two pointer solution - O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 0, 1
        
        while l < len(nums):
            if nums[l] != nums[r]:
                r += 1
            else:
                return nums[l]
            
            if r == len(nums):
                l += 1
                r = l + 1
                
# Floyd's tortoise and hare algo solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using floyds toroise and hare algo
        slow = nums[0]
        fast = nums[0]
        # when this loop breaks, both should be at meetup point
        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # second part of algo - start 1 pointer at head, other pointer at meetup point (can use slow or fast, they are both at meetup)        
        pointer1 = nums[0]
        pointer2 = slow
        # loop incrementing each pointer by 1 until they meet each other
        while pointer1 != pointer2:
            pointer1 = nums[pointer1]
            pointer2 = nums[pointer2]
            
        return pointer1

