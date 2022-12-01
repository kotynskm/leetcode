""" Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer."""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            curr_prod = 1

            for j in range(i, len(nums)):
                curr_prod *= nums[j]
                max_prod = max(curr_prod, max_prod)

        return max_prod