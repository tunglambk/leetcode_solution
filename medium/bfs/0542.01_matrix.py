class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if rows == 0:
            return []
        
        cols = len(mat[0])
        ret = [[0]*cols for _ in range(rows)]

        queue = deque()
        num_one = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c))
                elif mat[r][c] == 1:
                    num_one += 1
        
        time = 1
        while queue and num_one > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    xx, yy = x+dx, y+dy

                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    if mat[xx][yy] == 0:
                        continue
                    
                    ret[xx][yy] = time
                    mat[xx][yy] = 0
                    num_one -= 1
                    queue.append((xx, yy))

            time += 1
        return ret

