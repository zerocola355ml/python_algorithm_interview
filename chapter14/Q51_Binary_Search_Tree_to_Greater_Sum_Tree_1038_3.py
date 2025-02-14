# Answer2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root, curr):
            if not root:
                return curr
            root.val += helper(root.right, curr)
            return helper(root.left, root.val)
        helper(root, 0)
        return root