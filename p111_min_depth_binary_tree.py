# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        else:
            min_level, is_leaf = min_depth(root, 1)
            return min_level


def min_depth(root, level):
    if root == None:
        return level, False

    if not root.left and not root.right:
        return level, True
    else:
        level_left, leaf_left = min_depth(root.left, level + 1)
        level_right, leaf_right = min_depth(root.right, level + 1)

        if leaf_left and leaf_right:
            return (min(level_left, level_right), leaf_left)
        if leaf_left:
            return level_left, leaf_left
        if leaf_right:
            return level_right, leaf_right