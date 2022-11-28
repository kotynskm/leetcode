"""153. Find Minimum in Rotated Sorted Array
Medium
9.1K
439
company
Amazon
company
Microsoft
company
Apple
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 """

 class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            # if we are sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            
            # we are not sorted and need to search
            # calc the mid and update res potentially with smaller value at mid
            mid = (l + r)//2
            res = min(res, nums[mid])

            # are we on left side of nums ?
            if nums[l] <= nums[mid]:
                # search more right
                l = mid + 1
            else:
                # search more left
                r = mid - 1

        return res