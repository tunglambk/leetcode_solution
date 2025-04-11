class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        cons = [[] for _ in range(numCourses)]
        for item in prerequisites:
            in_degree[item[0]] += 1
            cons[item[1]].append(item[0])
        
        queue = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for item in cons[curr]:
                in_degree[item] -= 1
                if in_degree[item] == 0:
                    queue.append(item)
        if len(res) < numCourses:
            return []
        return res
