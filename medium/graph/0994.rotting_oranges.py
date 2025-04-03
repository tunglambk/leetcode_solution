class Solution:
    def _orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        queue = deque()
        num_orange = 0
        rotten = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    num_orange += 1
                    rotten.add(tuple([i, j]))
                if grid[i][j] == 1:
                    num_orange += 1
        
        if len(rotten) == num_orange:
            return 0

        visited = set()
        min_time = -1
        while queue:
            #current = queue.popleft()
            next_queue = deque()
            for item in queue:
                visited.add(tuple(item))
                if grid[item[0]][item[1]] == 1:
                    rotten.add(tuple(item))
                neighbors = self.get_valid_neighbor_positions(m, n, item[0], item[1])
                for neib in neighbors:
                    if neib not in queue and neib not in next_queue and neib not in visited and grid[neib[0]][neib[1]] == 1:
                        next_queue.append(neib)
            min_time += 1
            queue = next_queue

                    
        if len(rotten) < num_orange:
            return -1
        return min_time
        
    def get_valid_neighbor_positions(self, m, n, x, y):
    
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # top, left, right, bottom
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                neighbors.append((nx, ny))
        return neighbors
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return -1

        columns = len(grid[0])

        fresh_count = 0
        rotten = deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        min_time = 0
        while rotten and fresh_count > 0:
            min_time += 1

            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == rows or yy == columns or yy < 0:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    
                    fresh_count -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))
        return min_time if fresh_count == 0 else -1

