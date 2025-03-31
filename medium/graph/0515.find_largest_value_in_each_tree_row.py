# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        current_level = [root]
        max_val = []
        while current_level:
            next_level = []
            current_max = -2**31-1
            for node in current_level:
                current_max = max(current_max, node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            max_val.append(current_max)
            current_level = next_level
        return max_val

