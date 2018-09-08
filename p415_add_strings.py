def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """

    num1 = num1[::-1]
    num2 = num2[::-1]

    output = []
    i = 0
    j = 0
    carry = 0

    while i < len(num1) and j < len(num2):
        print
        "HERE"
        char1 = num1[i]
        char2 = num2[j]

        number1 = ord(char1) - ord('0')
        number2 = ord(char2) - ord('0')

        num_sum = number1 + number2 + carry
        if num_sum >= 10:
            digit = num_sum % 10
            carry = 1
        else:
            digit = num_sum
            carry = 0

        output.append(str(digit))
        i += 1
        j += 1

    while i < len(num1):
        char1 = num1[i]
        number1 = ord(char1) - ord('0')
        # print (number1, carry)
        num_sum = number1 + carry
        if num_sum >= 10:
            digit = num_sum % 10
            carry = 1
        else:
            digit = num_sum
            carry = 0

        output.append(str(digit))
        i += 1

    while j < len(num2):
        char2 = num2[j]
        number2 = ord(char2) - ord('0')
        # print (number2,carry)
        num_sum = number2 + carry
        if num_sum >= 10:
            digit = num_sum % 10
            carry = 1
        else:
            digit = num_sum
            carry = 0

        output.append(str(digit))
        j += 1

    if carry == 1:
        output.append(str(carry))

    return ''.join(reversed(output))


def main():
    print (addStrings("123456789", "987654321"))


if __name__ == "__main__":
    main()