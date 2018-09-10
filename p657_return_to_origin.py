def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """

    x = 0
    y = 0

    d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    for move in moves:
        coord = d[move]
        delta_x = coord[0]
        delta_y = coord[1]

        x += delta_x
        y += delta_y

    if x == 0 and y == 0:
        return True
    else:
        return False


def main():
    print (judgeCircle("UDL"))


if __name__ == "__main__":
    main()