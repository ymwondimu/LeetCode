"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        val = dfs(root)
        return val


def dfs(root):
    if len(root.children) == 0:
        return 1
    else:
        max_val = 0
        for child in root.children:
            subtree_depth = dfs(child)
            if max_val < subtree_depth:
                max_val = subtree_depth
        return 1 + max_val