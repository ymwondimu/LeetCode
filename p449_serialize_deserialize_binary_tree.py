# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return
        else:
            output = []

            tree_arr = self.preorder(root, output)
            return ' '.join(tree_arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        else:
            root = self.deserializeTree(data.split(), 0)[1]
            return root

    def deserializeTree(self, arr, i):
        if i >= len(arr) or arr[i] == "x":
            return [i + 1, None]
        else:
            node = TreeNode(arr[i])
            j, node.left = self.deserializeTree(arr, i + 1)
            j, node.right = self.deserializeTree(arr, j)

            return [j, node]

    def preorder(self, root, output):
        if root == None:
            output.append("x")
            return
        else:
            output.append(str(root.val))
            self.preorder(root.left, output)
            self.preorder(root.right, output)

        return output

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))