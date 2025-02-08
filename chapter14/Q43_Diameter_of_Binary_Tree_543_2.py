# Answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
		    # 여기에 diameter = 0 선언하면 오류 발생.
        def helper(root):
            if not root:
                return -1

            left = helper(root.left)
            right = helper(root.right)
            self.diameter = max(self.diameter, left + right + 2)

            return 1 + max(left, right)

        helper(root)

        return self.diameter