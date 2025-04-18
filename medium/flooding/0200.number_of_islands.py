class Solution:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1] 
    
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        count = 0

        visited = [[False]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if visited[r][c] or grid[r][c] == "0":
                    continue
                self.dfs(r, c, rows, cols, grid, visited)
                count += 1
        return count
        
    def dfs(self, x, y, rows, cols, grid, visited):
        visited[x][y] = True

        for i in range(4):
            u = x + self.dx[i]
            v = y + self.dy[i]
            if not self.inside(u, v, rows, cols) or visited[u][v] or grid[u][v] == "0":
                continue
            self.dfs(u, v, rows, cols, grid, visited)

    def inside(self, x, y, rows, cols):
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False
        return True
