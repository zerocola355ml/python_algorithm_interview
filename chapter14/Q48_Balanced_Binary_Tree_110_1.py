# My solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        if abs(depth(root.left) - depth(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)