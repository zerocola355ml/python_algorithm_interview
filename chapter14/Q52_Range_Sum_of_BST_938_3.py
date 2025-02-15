# My solution3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root):
            if not root:
                return 0
            if low <= root.val <= high:
                return root.val + helper(root.left) + helper(root.right)
            if root.val > high:
                return helper(root.left)
            if root.val < low:
                return helper(root.right)

        return helper(root)