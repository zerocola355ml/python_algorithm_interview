# Answer1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        def build(preorder, inorder):
            if inorder:
                index = inorder.index(preorder.popleft())
                node = TreeNode(inorder[index])
                node.left = build(preorder, inorder[0:index])
                node.right = build(preorder, inorder[index + 1:])
                return node
        return build(preorder, inorder)