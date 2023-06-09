# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = []

        def in_order(r):
            if r:
                in_order(r.left)
                if len(queue) < k:
                    queue.append(r.val)
                in_order(r.right)

        in_order(root)

        return queue.pop()