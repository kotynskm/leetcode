""" Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time. """

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set to check for consecutive numbers
        num_set = set(nums)
        # initialize longest variable
        longest = 0
        
        # loop nums and check if num is the start of a sequence (has no left neighbor)
        for n in nums:
            if (n - 1) not in num_set:
                # initialize length
                length = 0
                # check for consecutive nums
                while (n + length) in num_set:
                    # increment the length
                    length +=1
                # update longest
                longest = max(length, longest)
        return longest