# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = level_order(root)
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = res[i][::-1]

        return res


def level_order(root):
    q, result = deque(), []
    q = deque()
    if root:
        q.append(root)
    while len(q):
        level = []
        for _ in range(len(q)):
            x = q.popleft()
            level.append(x.val)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        result.append(level)

    return result