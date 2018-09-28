def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    nums = sorted(nums)
    output = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -1 * nums[i]
        start = i + 1
        end = n - 1

        while start < end:
            if nums[start] + nums[end] == target:
                output.append([nums[i], nums[start], nums[end]])
                start += 1

                while start < end and nums[start] == nums[start - 1]:
                    start += 1
            elif nums[start] + nums[end] < target:
                start += 1

            else:
                end -= 1

    return output


def threeSumAll(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    nums = sorted(nums)
    output = []
    n = len(nums)

    for i in range(n):

        target = -1 * nums[i]
        start = i + 1
        end = n - 1

        while start < end:
            if nums[start] + nums[end] == target:
                output.append([i, start, end])
                start += 1

            elif nums[start] + nums[end] < target:
                start += 1

            else:
                end -= 1

    return output

def main():
    nums = [-1, 0, 1, 2, -1, -4]
    print (threeSumAll(nums))


if __name__ == "__main__":
    main()