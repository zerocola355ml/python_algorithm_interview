# Answer1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    path = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.path = max(self.path, left + right)
            return max(left, right)

        helper(root)
        return self.path