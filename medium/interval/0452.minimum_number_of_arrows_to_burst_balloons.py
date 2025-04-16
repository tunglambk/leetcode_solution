class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        end = points[0][1]
        cnt = 1

        for inv in points[1:]:
            if inv[0] <= end:
                end = min(inv[1], end)
            else:
                end = inv[1]
                cnt += 1
        return cnt
