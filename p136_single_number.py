def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    res = 0
    for num in nums:
        res ^= num

    return res


def main():
    print (singleNumber([3,3,5,5,7]))


if __name__ == "__main__":
    main()
