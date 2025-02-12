# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []

        def helper(root):
            if not root:
                result.append('null')
                return
            result.append(str(root.val))
            helper(root.left)
            helper(root.right)

        helper(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        result = collections.deque(data.split(','))

        def helper(val):
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = helper(result.popleft())
            node.right = helper(result.popleft())
            return node

        return helper(result.popleft())

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))