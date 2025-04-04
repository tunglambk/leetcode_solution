class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(0, rooms, visited)

        if len(visited) == len(rooms):
            return True
        return False

    def dfs(self, curr, rooms, visited):
        visited.add(curr)
        for item in rooms[curr]:
            if item in visited:
                continue
            self.dfs(item, rooms, visited)

