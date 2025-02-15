# Answer2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -float("inf")
        result = float("inf")
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result = min(result, node.val - prev)
            prev = node.val
            node = node.right
        return result