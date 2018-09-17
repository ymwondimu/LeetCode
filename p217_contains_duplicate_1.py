def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # if len(nums) == 0:
    #    return False

    d = {}
    for num in nums:
        if num not in d:
            d[num] = 1
        else:
            return True
    return False


def main():
    nums = [1,9,3,9,2,5]
    print (containsDuplicate(nums))

if __name__ == "__main__":
    main()