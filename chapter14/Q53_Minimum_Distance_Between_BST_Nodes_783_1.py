# My solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def right_min(root):
            if not root:
                return 0
            while root.left:
                root = root.left
            return root.val
        def left_max(root):
            if not root:
                return 0
            while root.right:
                root = root.right
            return root.val
        def helper(root):
            curr = float("inf")
            if root:
                if root.left:
                    curr = min(curr, root.val - left_max(root.left), helper(root.left))
                if root.right:
                    curr = min(curr, right_min(root.right) - root.val, helper(root.right))
            return curr
        return helper(root)