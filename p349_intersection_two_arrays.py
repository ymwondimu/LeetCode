from collections import Counter

def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    if len(nums1) == 0 or len(nums2) == 0:
        return []

    d = Counter(nums1)
    output = set()
    for num in nums2:
        if num in d:
            output.add(num)

    return list(output)


def main():
    arr1 = [1,2,2,1]
    arr2 = [2,2]

    print (intersection(arr1, arr2))


if __name__ == "__main__":
    main()