def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    i = 0
    zero_count = 0

    for num in nums:
        if num != 0:
            nums[i] = num
            i += 1
        else:
            zero_count += 1

    if len(nums) > 1 and zero_count > 0:
        nums[-zero_count:] = [0] * zero_count


def main():
    nums = [0,1,0,2,3]
    moveZeroes(nums)
    print (nums)


if __name__ == "__main__":
    main()