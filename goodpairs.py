""" Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 """

 class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0

        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i + 1, len(nums)):
                num2 = nums[j]

                if num1 == num2:
                    pairs += 1

        return pairs
