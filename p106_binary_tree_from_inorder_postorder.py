# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if not inorder or not postorder:
            return None

        val = postorder[-1]
        node = TreeNode(val)

        index = 0
        for i in range(len(inorder)):
            num = inorder[i]
            if num == val:
                index = i

        node.left = self.buildTree(inorder[:index], postorder[:index])
        node.right = self.buildTree(inorder[index + 1:], postorder[index:-1])

        return node