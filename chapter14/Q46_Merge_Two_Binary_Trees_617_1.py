# My solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root2:
            return root1
        if not root1:
            return root2
        result = root1

        def helper(node1, node2):
            if node1 == node2:  # Include None Case
                return
            if not node2:
                return
            node1.val += node2.val
            if not node1.left and node2.left:
                node1.left = node2.left
            else:
                helper(node1.left, node2.left)
            if not node1.right and node2.right:
                node1.right = node2.right
            else:
                helper(node1.right, node2.right)

        helper(root1, root2)
        return result