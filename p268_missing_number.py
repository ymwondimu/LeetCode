def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    n = len(nums) + 1
    total = (n * (n - 1)) / 2

    for val in nums:
        total -= val

    return int(total)


def main():
    arr = [9,6,4,2,3,5,7,0,1]
    print (missingNumber(arr))


if __name__ == "__main__":
    main()