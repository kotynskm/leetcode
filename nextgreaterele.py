""" The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above."""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # make a dict with nums1 values and their index, we need the index for the result output
        d = {index:num for num, index in enumerate(nums1)}
        # populate res with -1s and will replace with greater value if found
        res = [-1] * len(nums1)
        
        # iterate nums2 and check if value is in dict
        for i in range(len(nums2)):
            if nums2[i] in d:
                # if value is in dict, then loop at i + 1 to check for greater value
                for j in range(i + 1, len(nums2)):
                    # if greater val found, get the appropriate index from d, then set result at index to the greater value
                    if nums2[j] > nums2[i]:
                        index = d[nums2[i]]
                        res[index] = nums2[j]
                        break;
        return res