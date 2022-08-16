""" Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums. """

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total_sum = 0
        
        # loop and calculate the sum, append to result
        for num in nums:
            total_sum += num
            result.append(total_sum)
            
        return result