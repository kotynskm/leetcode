""" Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is 

equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 

This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1. """

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # set left_sum variable and total
        left_sum = 0
        total = sum(nums)
        
        # loop and calculate left_sum, check if left_sum equals right_sum
        for i, num in enumerate(nums):
            # right_sum is the total minus the left sum minus the current num
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1