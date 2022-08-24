""" The majority element is the element that appears more than ⌊n / 2⌋ times. 

You may assume that the majority element always exists in the array. """

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hash table
        num_counts = {}
        # target count we are looking for for majority element
        target_count = len(nums)//2
        
        # populate hash table
        for i in range(len(nums)):
            num_counts[nums[i]] = 1 + num_counts.get(nums[i], 0)
        
        # loop keys and values and compare value to target count, return the majority element which is our key
        for key, val in num_counts.items():
            if val > target_count:
                ele = key
                
        return ele

    # O(n) time and O(1) space solution
    class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # set result and count variables
        res, count = 0,0
        
        # loop through nums
        for n in nums:
            # if count is 0, result is set to n
            if count == 0:
                res = n
            
            # if n equals result, then increment the count, else decrement
            if n == res:
                count += 1
            else:
                count -= 1
        return res