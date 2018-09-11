def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums = sorted(nums)
    res = 0
    for i in range(0, len(nums), 2):
        x = nums[i]
        y = nums[i + 1]

        delta = min(x, y)
        res += delta

    return res


def main():
    print (arrayPairSum([1,3,4,2]))


if __name__ == "__main__":
    main()
