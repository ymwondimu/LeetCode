# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        level, balanced = in_order(root)
        # print (level, balanced)
        return balanced


def in_order(root):
    if root == None:
        return (0, True)
    else:
        level_left, balanced_left = in_order(root.left)
        level_right, balanced_right = in_order(root.right)
        max_level = 1 + max(level_left, level_right)
        is_balanced = (abs(level_left - level_right) <= 1) and (balanced_left and balanced_right)
        return (max_level, is_balanced)