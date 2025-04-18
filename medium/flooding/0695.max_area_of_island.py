class Solution:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False]*n for _ in range(m)]
        max_area = 0
        for x in range(m):
            for y in range(n):
                if visited[x][y] or grid[x][y] == 0:
                    continue
                area = self.dfs(x, y, m, n, grid, visited)
                max_area = max(max_area, area)
        return max_area

    def dfs(self, x, y, m, n, grid, visited):
        visited[x][y] = True
        val = 1
        for i in range(4):
            u = x + self.dx[i]
            v = y + self.dy[i]
            if not self.inside(u, v, m, n) or visited[u][v] or grid[u][v] == 0:
                continue
            val += self.dfs(u, v, m, n, grid, visited)
        return val

    def inside(self, x, y, m, n):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        return True
