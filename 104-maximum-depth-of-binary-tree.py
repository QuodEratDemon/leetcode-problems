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

        max_left = Solution.maxDepth(self, root.left) + 1
        max_right = Solution.maxDepth(self, root.right) + 1

        return max(max_left, max_right)