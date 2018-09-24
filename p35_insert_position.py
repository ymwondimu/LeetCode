def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if len(nums) == 0:
        return 0

    for i, num in enumerate(nums):
        if num >= target:
            return i

    return len(nums)


def main():
    input = [1,3,5,6]
    targets = [5,2,7,0]

    for target in targets:
        print (searchInsert(input,target))


if __name__ == "__main__":
    main()