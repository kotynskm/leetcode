class Solution:
    def twoSum(self, nums, target): 
        # loop and get first num
        for i in range(0, len(nums)):
        # loop and get second num
            for j in range(i+1, len(nums)):
                # does sum of num[i] and num[j] == target? if so, return i and j  
                if nums[i] + nums[j] == target:
                    return i,j