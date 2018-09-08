from collections import Counter

def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """

    d = Counter(J)

    count = 0

    for char in S:
        if char in d:
            count += 1

    return count


def main():
    print (numJewelsInStones("aA","aAAbbbb"))


if __name__ == "__main__":
    main()