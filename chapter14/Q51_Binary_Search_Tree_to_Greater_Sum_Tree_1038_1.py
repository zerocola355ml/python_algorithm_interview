# My solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = 0
        def helper(root):
            nonlocal curr
            if not root:
                return
            helper(root.right)
            root.val, curr = root.val + curr, curr + root.val
            helper(root.left)
        helper(root)
        return root