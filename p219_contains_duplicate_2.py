def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """

    d = {}

    for i in range(len(nums)):
        num = nums[i]
        if num not in d:
            d[num] = i
        else:
            j = d[num]
            if abs(i - j) <= k:
                return True
            else:
                d[num] = i

    return False


def main():
    nums = [1,2,3,1,2,3]
    k = 2
    print (containsNearbyDuplicate(nums, k))


if __name__ == "__main__":
    main()