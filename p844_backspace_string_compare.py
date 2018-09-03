def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """

    res1 = create_stack(S)
    res2 = create_stack(T)

    return res1 == res2


def create_stack(s):
    stack = []
    for char in s:
        if char == "#":

            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(char)
    return "".join(stack)


def main():
    pass


if __name__ == "__main__":
    main()
