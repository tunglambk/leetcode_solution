class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if len(isConnected) == 0:
            return 0

        visited = set()
        num_province = 0

        for current_city in range(len(isConnected)):
            if current_city in visited:
                continue
            queue = []
            queue.append(current_city)
            while queue:
                next_queue = []
                for i in queue:
                    if i not in visited:
                        visited.add(i)
                        for j in range(len(isConnected[i])):
                            if isConnected[i][j] == 1 and j not in visited:
                                next_queue.append(j)
                queue= next_queue
            num_province += 1
        return num_province
