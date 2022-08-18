""" Given two integer arrays nums1 and nums2, return an array of their intersection. 

Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = {}, {}
        result = []
        
        # make hash tables for both lists
        for i in range(len(nums1)):
            count1[nums1[i]] = 1 + count1.get(nums1[i], 0)
            
        for i in range(len(nums2)):
            count2[nums2[i]] = 1 + count2.get(nums2[i], 0)
            
        # check if keys are a match
        for key in count1:
            if key in count2:
                # use min to get the minimum number between the counts
                count = min(count1[key], count2[key])
                for i in range(count):
                    result.append(key)
                    
        return result
