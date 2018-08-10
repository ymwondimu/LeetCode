# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        output = []
        in_order(root, output)

        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False

        return True


def in_order(root, output):
    if root == None:
        return
    else:
        in_order(root.left, output)
        output.append(root.val)
        in_order(root.right, output)