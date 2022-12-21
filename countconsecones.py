""" Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2 """

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #loop and keep track of the longest streak of 1s
        #iterate and if num is 1, increase curr count
        #update max
        #else it's not a 1, reset the count to 0
        
        max_count = 0
        curr_count = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count += 1
                max_count = max(curr_count, max_count)
            else:
                curr_count = 0
                
        return max_count