class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals.sort()
        prev_end = -1

        for interval in intervals:
            start, end = interval
            if start < prev_end:
                return False

            prev_end = end

        return True