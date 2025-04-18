class Solution:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])

        visited = [[False]*n for _ in range(m)]
        num_sub = 0
        for x in range(m):
            for y in range(n):
                if visited[x][y] or grid2[x][y] == 0:
                    continue
                if self.dfs(x, y, m, n, grid1, grid2, visited):
                    num_sub += 1
        
        return num_sub

    def dfs(self, x, y, m, n, grid1, grid2, visited):
        visited[x][y] = True
        val = grid1[x][y] == 1
        for i in range(4):
            u = x + self.dx[i]
            v = y + self.dy[i]
            if not self.inside(u, v, m, n) or visited[u][v] or grid2[u][v] == 0:
                continue
            val = val & self.dfs(u, v, m, n, grid1, grid2, visited)
        return val

    def inside(self, x, y, m, n):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        return True
