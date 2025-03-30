# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None and q != None or p != None and q == None:
            return False
        if p.val != q.val:
            return False
        same_left = self.isSameTree(p.left, q.left)
        same_right = self.isSameTree(p.right, q.right)
        return same_left and same_right
        
