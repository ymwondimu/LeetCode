# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        output = []
        search(root, output, "")
        return (output)


def search(root, output, s):
    if not root.left and not root.right:
        output.append(s + str(root.val))
    if root.left:
        search(root.left, output, s + str(root.val) + '->')
    if root.right:
        search(root.right, output, s + str(root.val) + '->')
