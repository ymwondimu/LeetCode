def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    left = 0
    right = len(nums) - 1

    while (left <= right):
        mid = (right + left) // 2

        if nums[mid] < target:
            left = mid + 1

        elif nums[mid] > target:
            right = mid - 1

        else:
            while (nums[left] != target):
                left += 1

            while (nums[right] != target):
                right -= 1

            return [left, right]

    return [-1, -1]


def main():
    arr = [5,7,7,8,8,10]
    target = 8

    print (searchRange(arr,target))


if __name__ == "__main__":
    main()