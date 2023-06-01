# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p and q:
            same_left = Solution.isSameTree(self, p.left, q.left)
            same_right = Solution.isSameTree(self, p.right, q.right)
        elif not p and not q:
            return True
        else: 
            return False

        return same_left and same_right and p.val == q.val