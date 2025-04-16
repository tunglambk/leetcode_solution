class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = len(intervals)
        if l == 0:
            return [newInterval]
        idx = 0
        for i in range(l):
            if newInterval[0] >= intervals[i][0]:
                idx = i+1
            else:
                break
        #idx = bisect.bisect_left(intervals, newInterval)
        merged = intervals[:idx-1] if idx > 0 else []

        if idx > 0:
            if self.overlap(intervals[idx-1], newInterval):
                newInterval[0] = min(newInterval[0], intervals[idx-1][0])
                newInterval[1] = max(newInterval[1], intervals[idx-1][1])
            else:
                merged.append(intervals[idx-1])
        while idx < len(intervals):
            if self.overlap(intervals[idx], newInterval):
                newInterval[0] = min(newInterval[0], intervals[idx][0])
                newInterval[1] = max(newInterval[1], intervals[idx][1])
            else:
                merged.append(newInterval)
                break
            idx += 1
        if idx == l:
            merged.append(newInterval)
        else:
            merged.extend(intervals[idx:])
        return merged
    
    def overlap(self, invA, invB):
        if (invA[1] >= invB[0] and invA[0] <= invB[0]) or (invB[1] >= invA[0] and invB[0] <= invA[0]):
            return True
        return False

