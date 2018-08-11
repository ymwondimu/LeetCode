# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        else:
            return hasPathSum(root, sum)


def hasPathSum(root, sum):
    if not root:
        return False
    if root.val - sum == 0 and not root.left and not root.right:
        return True
    else:
        return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)