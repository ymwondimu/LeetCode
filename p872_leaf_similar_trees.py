# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        output1 = []
        output2 = []
        in_order(root1, output1)
        in_order(root2, output2)

        if output1 == output2:
            return True
        else:
            return False


def in_order(root, output):
    if root == None:
        return
    else:
        in_order(root.left, output)
        if not root.left and not root.right:
            output.append(root.val)
        in_order(root.right, output)