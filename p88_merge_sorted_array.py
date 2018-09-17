def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """

    index1 = m - 1
    index2 = n - 1
    target = n + m - 1

    while (index1 > -1 and index2 > -1):
        if nums1[index1] > nums2[index2]:
            nums1[target] = nums1[index1]
            index1 -= 1
            target -= 1
        else:
            nums1[target] = nums2[index2]
            index2 -= 1
            target -= 1

    while index1 > -1:
        nums1[target] = nums1[index1]
        index1 -= 1
        target -= 1

    while index2 > -1:
        nums1[target] = nums2[index2]
        index2 -= 1
        target -= 1


def main():
    m = 3
    n = 3
    nums1 = [1,2,3, 0, 0, 0]
    nums2 = [2,5,6]

    merge(nums1, m, nums2, n)
    print (nums1)


if __name__ == "__main__":
    main()