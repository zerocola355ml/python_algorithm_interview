# Answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right)+1
        return depth(root) != -1