# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        output = []
        output2 = []
        in_order(p, output)
        in_order(q, output2)

        print(output)
        print(output2)

        if output == output2:
            return True
        else:
            return False


def in_order(root, output):
    if root == None:
        output.append("null")
        return None
    else:
        output.append(root.val)
        in_order(root.left, output)
        # print (root.val)
        in_order(root.right, output)