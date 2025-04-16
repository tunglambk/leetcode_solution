class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        cnt = 1
        end = intervals[0][1]

        for inv in intervals:
            if inv[0] < end:
                end = min(end, inv[1])
            else:
                cnt += 1
                end = inv[1]
        return len(intervals) - cnt
