# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        max_depth = 0
        
        while queue:
            next_layer = deque()
            for item in queue:
                if item.left:
                    next_layer.append(item.left)
                if item.right:
                    next_layer.append(item.right)
            queue=next_layer
            max_depth += 1
        return max_depth
