"""Given a 32-bit signed integer, reverse digits of an integer."""

def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    bounds = (2**31)-1
    string_x = str(x)
    reversed_x = string_x[::-1]


    if (x<0):
        reversed_int = -1*int(reversed_x[:-1])
    else:
        reversed_int = int(reversed_x)

    if (reversed_int > bounds) or (reversed_int < -1 * bounds):
        return 0
    else:
        return reversed_int


def main():
    print (reverse(-1234567798123))

if __name__ == "__main__":
    main()