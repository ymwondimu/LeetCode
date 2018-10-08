def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    s, e = 0, 0

    for i in range(len(nums)):
        # T[i] = max(T[i-2] + nums[i], T[i-1])
        s, e = e, max(s + nums[i], e)

    return e


def main():
    arr = [2, 7, 9, 3, 1]
    print (rob(arr))


if __name__ == "__main__":
    main()