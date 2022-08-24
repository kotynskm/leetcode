""" Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space. """

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # set result variable, use 0 b/c n ^ 0 = n
        result = 0
        
        # loop nums and do XOR
        for n in nums:
            # result will only become the value of the unique num, because for each duplicate value, the result will be reset to 0, any number XOR itself will result in 0
            result = n ^ result
            
        return result