class Solution:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        
        found = False
        x = 0
        queue = deque()
        while not found and x < n:
            y = 0
            while not found and y < n:
                if grid[x][y]==1:
                    self.dfs(x, y, n, grid, visited, queue)
                    found = True
                y += 1
            x += 1
        
        res = 0

        while queue:
            next_queue = deque()
            for item in queue:
                for i in range(4):
                    u = item[0] + self.dx[i]
                    v = item[1] + self.dy[i]
                    if not self.inside(u, v, n) or visited[u][v]:
                        continue
                    if grid[u][v] == 1:
                        queue = deque()
                        return res
                    visited[u][v] = True
                    next_queue.append([u, v])
            res += 1
            queue = next_queue
        queue = deque()
        return -1
                    

    
    def dfs(self, x, y, n, grid, visited, queue):
        visited[x][y] = True
        queue.append([x,y])
        for i in range(4):
            u = x + self.dx[i]
            v = y + self.dy[i]
            if not self.inside(u, v, n) or visited[u][v] or grid[u][v] == 0:
                continue
            self.dfs(u, v, n, grid, visited, queue)
    
    def inside(self, x, y, n):
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        return True
