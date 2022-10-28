""" Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input. """

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals list
        # initialze merged meetings list with the first meeting
        # loop and compare the end time of prev meeting, to start time of the next meeting
        # if end time > start time of next meeting - they overlap, so merge them by using start time of first meeting, end time of the next meeting
        # time complexity O(nlogn)
        
        sorted_meetings = sorted(intervals)
        # put in the first meeting initially (edge case)
        merged_meetings = [sorted_meetings[0]]
        
        # unpack start and end value and iterate intervals from 1
        for current_start, current_end in sorted_meetings[1:]:
            # compare end time of the last merged meeting to the start time of next meeting
            last_end_time = merged_meetings[-1][1]
            if last_end_time >= current_start:
                # merge the meeting, the last meeting in the list leave the start time and replace the end time with max end time bt meetings
                merged_meetings[-1][1] = max(current_end,last_end_time)
            else:
                merged_meetings.append([current_start,current_end])
        return merged_meetings