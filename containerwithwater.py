""" You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container. """

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #l,r pointers
        #loop and calculate the length using the index
        #multiply the length by the height
        #update max
        #update the pointers, whichever is lower moves forward

        l,r = 0, len(height) - 1
        max_vol = 0

        while l <= r:
            #calc the length using the index (because we are doing an area calculation)
            length = r - l
            #calc the volume
            volume = min(height[l],height[r]) * length
            #update max
            max_vol = max(max_vol, volume)
            #update pointers
            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return max_vol