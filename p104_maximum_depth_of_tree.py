# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        md = max_depth(root, 1)
        print(md)
        return md


def max_depth(root, level):
    if root == None:
        return level
    else:
        if root.left and root.right:
            level_left = max_depth(root.left, level + 1)
            level_right = max_depth(root.right, level + 1)
            return max(level_left, level_right)
        if root.left:
            return max_depth(root.left, level + 1)
        if root.right:
            return max_depth(root.right, level + 1)
        if not root.left and not root.right:
            return level