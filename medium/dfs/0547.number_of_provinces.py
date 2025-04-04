class Solution:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = set()
        for item in range(len(isConnected)):
            if item not in visited:
                count += 1
                self.dfs(item, isConnected, visited)
        return count
    
    def dfs(self, curr, isConnected, visited):
        visited.add(curr)
        for item in range(len(isConnected[curr])):
            if item in visited or isConnected[curr][item] == 0:
                continue
            self.dfs(item, isConnected, visited)
