""" Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array. """

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # set value for maximum sum and the current sum
        max_sum = nums[0]
        curr_sum = 0
        
        # loop over nums and calculate curr_sum and max_sum
        for num in nums:
            # if the sum is a negative value, we don't want to keep it
            if curr_sum < 0:
                curr_sum = 0
            # add the next num    
            curr_sum += num
            # find the max sum
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
                