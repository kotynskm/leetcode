""" Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        min_length = len(nums) + 1
        sum = 0

        for end in range(len(nums)):
            sum += nums[end]
            # if sum ever >= target update the min length and update the start pointer
            while sum >= target:
                min_length = min(min_length, end-start + 1)
                sum -= nums[start]
                start += 1

        return 0 if min_length == len(nums) + 1 else min_length