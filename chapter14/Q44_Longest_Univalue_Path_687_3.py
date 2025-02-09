# Answer2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0

        def dfs(root):
            nonlocal res
            if not root: return 0
            if not root.left and not root.right: return 0
            left_len = dfs(root.left)
            right_len = dfs(root.right)
            if root.left and root.right and root.right.val == root.left.val == root.val:
                res = max(res, left_len + right_len + 2)
                return max(left_len, right_len) + 1
            if root.right and root.right.val == root.val:
                right_len += 1
                res = max(res, right_len)
                return right_len
            if root.left and root.left.val == root.val:
                left_len += 1
                res = max(res, left_len)
                return left_len
            return 0

        dfs(root)
        return res

