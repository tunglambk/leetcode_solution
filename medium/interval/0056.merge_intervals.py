class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merged = []

        curr = intervals[0]
        for inv in intervals[1:]:
            if self.overlap(curr, inv):
                curr[1] = max(curr[1], inv[1])
            else:
                merged.append(curr)
                curr = inv
        merged.append(curr)
        return merged
    
    def overlap(self, invA, invB):
        if invA[0] <= invB[1] and invA[1] >= invB[0]:
            return True
        return False
