# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        output = []

        in_order(root, output)

        ht = {}
        for val in output:
            if (k - val) in ht:
                return True
            else:
                ht[val] = 1

        return False


def in_order(root, output):
    if root == None:
        return
    else:
        in_order(root.left, output)
        output.append(root.val)
        in_order(root.right, output)