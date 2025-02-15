# My solution1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        cnt = 0

        def helper(root):
            nonlocal cnt
            if not root:
                return
            if low <= root.val <= high:
                cnt += root.val
            if root.val > high:
                helper(root.left)
                return
            if root.val < low:
                helper(root.right)
                return
            helper(root.left)
            helper(root.right)
            return

        helper(root)
        return cnt