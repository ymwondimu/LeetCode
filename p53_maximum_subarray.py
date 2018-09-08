def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    T = [0] * len(nums)
    T[0] = nums[0]

    for i in range(1, len(nums)):
        if T[i - 1] + nums[i] > nums[i]:
            T[i] = T[i - 1] + nums[i]
        else:
            T[i] = nums[i]

    return max(T)


def main():
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


if __name__ == "__main__":
    main()