""" Given an array of integers nums which is sorted in ascending order, and an integer target, write a function 

to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity. """

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set left and right pointers
        l, r = 0, len(nums) - 1
        
        # loop while l < r
        while l <= r:
            # calculate the middle index
            mid_index = (l + r)//2
            
            # check if num at middle index is target, less than, or greater than target
            if nums[mid_index] == target:
                return mid_index
            # the r index must be updated to the middle - 1 to eliminate the right side values
            if target < nums[mid_index]:
                r = mid_index - 1
            # the l index must be updated to the middle + 1 to eliminate the left side values  
            if target > nums[mid_index]:
                l = mid_index + 1
                
        return -1
        