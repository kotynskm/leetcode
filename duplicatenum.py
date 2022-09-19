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
                

