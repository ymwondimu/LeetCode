# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder or not inorder:
            return None

        val = preorder[0]
        node = TreeNode(val)

        index = 0
        for i in range(len(inorder)):
            num = inorder[i]
            if num == val:
                index = i

        preorder = preorder[1:]
        node.left = self.buildTree(preorder[:index], inorder[:index])
        node.right = self.buildTree(preorder[index:], inorder[index + 1:])

        return node