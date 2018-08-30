def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    curr_index = 0
    count = 1
    for i in range(1, len(nums)):

        if nums[i] != nums[curr_index]:
            curr_index += 1
            nums[curr_index] = nums[i]
            count += 1

    return nums[:count]


def main():
    val1 = removeDuplicates([0,0,1,1,1,1,2,2,3,3,5,5,5,8,8,9,10,12])
    print (val1)


if __name__ == "__main__":
    main()