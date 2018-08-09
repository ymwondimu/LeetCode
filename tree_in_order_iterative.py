def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    stack = []
    node = root
    done = False

    output = []

    while (not done):
        if node is not None:
            stack.append(node)
            node = node.left

        else:
            if len(stack) > 0:
                node = stack.pop()
                output.append(node.val)
                node = node.right

            else:
                done = True

    return output

if __name__ == "__main__":
    main()