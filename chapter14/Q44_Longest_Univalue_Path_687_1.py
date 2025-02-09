# My solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    path = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return -1
            left = -1
            right = -1
            if root.left:
                tempL = helper(root.left)
                if root.left.val == root.val:
                    left = tempL
                    self.path = max(self.path, tempL + 1)
            if root.right:
                tempR = helper(root.right)
                if root.right.val == root.val:
                    right = tempR
                    self.path = max(self.path, tempR + 1)
            if root.left and root.right and root.left.val == root.right.val == root.val:
                self.path = max(self.path, tempL + tempR + 2)
            depth = 1 + max(left, right)
            return depth
        helper(root)
        return self.path