class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        states = [None]*n
        path = set()

        def dfs(curr):
            if curr in path:
                return False
            if states[curr] != None:
                return states[curr]
            path.add(curr)
            for next_node in graph[curr]:
                if not dfs(next_node):
                    states[next_node] = False
                    path.remove(curr)
                    return False
            path.remove(curr)
            states[curr] = True
            return True
        
        ret = []
        for i in range(n):
            if dfs(i):
                ret.append(i)

        return ret

