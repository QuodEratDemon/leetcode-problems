class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        queue = []
        
        for interval in intervals:
            if not queue:
                heapq.heappush(queue, interval[1])
            else:
                curr = heapq.heappop(queue)
                if interval[0] < curr:
                    heapq.heappush(queue, curr)
                heapq.heappush(queue, interval[1])
        
                
        return len(queue)