class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        def dfs(curr, graph, colors, color):
            if colors[curr] != 0:
                return color == colors[curr]
            colors[curr] = color
            if color == 1:
                next_color = 2
            else:
                next_color = 1
            for next_node in graph[curr]:
                if not dfs(next_node, graph, colors, next_color):
                    return False
            return True

        for i in range(n):
            if colors[i] != 0:
                continue
            if not dfs(i, graph, colors, 1):
                return False
        return True
