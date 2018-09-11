from collections import Counter

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    d = Counter(nums)

    max_val = 0
    max_count = -float('inf')

    for value, count in d.items():
        if count > max_count:
            max_val = value
            max_count = count

    return max_val


def main():
    print (majorityElement([1,2,3,4,1,2,3,4,4]))


if __name__ == "__main__":
    main()