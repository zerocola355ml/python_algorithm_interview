# My solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            left = (0, 0)
            right = (0, 0)
            if not root:
                return (0, 0)
            if root.left:
                left = helper(root.left)
            if root.right:
                right = helper(root.right)

            diameter = max(left[0], right[0], left[1] + right[1])
            depth = 1 + max(left[1], right[1])

            return (diameter, depth)

        return helper(root)[0]