"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def _maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        max_depth = 0
        for i in range(len(root.children)):
            max_depth = max(max_depth, self.maxDepth(root.children[i]))
        return 1 + max_depth

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        nodes = deque()
        nodes.append((root, 1))
        maxx = 0
        while nodes:
            cur, val = nodes.popleft()
            maxx = val
            if cur.children:
                for child in cur.children:
                    nodes.append((child, val+1))
        return maxx
