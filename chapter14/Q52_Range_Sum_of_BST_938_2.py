# My solution2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root, cnt):
            if not root:
                return 0
            if low <= root.val <= high:
                return cnt + root.val + helper(root.left, cnt) + helper(root.right, cnt)
            if root.val > high:
                return cnt + helper(root.left, cnt)
            if root.val < low:
                return cnt + helper(root.right, cnt)

        return helper(root, 0)