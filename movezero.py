""" Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array. """

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use two pointers
        ind1, ind2 = 0, len(nums) + 1
        
        # loop while ind1 < length of input
        while ind1 < len(nums):
            # if the num is a zero, insert it at the last index, and remove from the list
            if nums[ind1] == 0:
                nums.insert(ind2, nums[ind1])
                nums.remove(nums[ind1])
                ind1 += 1
            else:
                ind1 += 1
        return nums

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # keeps track of where to insert number
        l = 0
        
        # loop
        # check if number is NOT a zero
        # if not a zero, swap with value at l pointer and increment l pointer
        # else continue looping
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1