def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    digits = digits[::-1]
    carry = 0

    if digits[0] != 9:
        digits[0] = digits[0] + 1
        return digits[::-1]
    else:
        carry = 1
        digits[0] = 0
        for i in range(1, len(digits)):
            x = digits[i]
            sum_dig = digits[i] + carry
            if sum_dig >= 10:
                carry = 1
            else:
                carry = 0
            digits[i] = sum_dig % 10

        if carry == 1:
            digits.append(carry)

    return digits[::-1]


def main():
    print (plusOne([9,9]))


if __name__ == "__main__":
    main()
