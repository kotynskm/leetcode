""" Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings. """

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_ints = sorted(intervals)

        for i in range(len(sorted_ints) - 1):
            if sorted_ints[i][1] > sorted_ints[i + 1][0]:
                return False
        
        return True