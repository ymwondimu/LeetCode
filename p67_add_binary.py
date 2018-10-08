def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """

    a = a[::-1]
    b = b[::-1]

    p1 = 0
    p2 = 0

    output = ""
    carry = 0

    while (p1 < len(a) and p2 < len(b)):
        sum_val = int(a[p1]) + int(b[p2]) + carry
        if sum_val >= 2:
            carry = 1
        else:
            carry = 0
        val = sum_val % 2
        output += str(val)
        p1 += 1
        p2 += 1

    if p1 == len(a):
        while (p2 < len(b)):
            sum_val = carry + int(b[p2])
            if sum_val >= 2:
                carry = 1
            else:
                carry = 0

            val = sum_val % 2
            output += str(val)
            p2 += 1

    if p2 == len(b):
        while (p1 < len(a)):
            sum_val = carry + int(a[p1])
            if sum_val == 2:
                carry = 1
            else:
                carry = 0

            val = sum_val % 2
            output += str(val)
            p1 += 1

    if carry == 1:
        output += str(carry)

    return output[::-1]


def main():
    a = "1010"
    b = "1011"
    print (addBinary(a,b))


if __name__ == "__main__":
    main()