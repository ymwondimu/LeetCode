def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    return points(numbers, target)
    #return dic(numbers, target)


def points(numbers, target):
    i = 0
    j = len(numbers) - 1

    while (i < j):
        sum = numbers[i] + numbers[j]
        if sum == target:
            return i + 1, j + 1
        elif sum < target:
            i += 1
        else:
            j -= 1


def dic(numbers, target):
    ht = {}

    for i in range(1, len(numbers) + 1):
        diff = target - numbers[i - 1]
        if diff in ht:
            return ht[diff], i
        else:
            ht[numbers[i - 1]] = i


def main():
    numbers = [2,7,11,15]
    target = 9
    print (twoSum(numbers, target))


if __name__ == "__main__":
    main()