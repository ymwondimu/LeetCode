def is_palindrome(x):
    b1 = nonstring_palindrome(x)
    b2 = string_palindrome(x)

    return b1


def string_palindrome(x):
    num = str(x)
    return num == num[::-1]


def nonstring_palindrome(x):
    if x < 0:
        return False
    else:
        res = x
        total = 0
        while (res):
            total = total * 10 + res % 10
            res //= 10

        print (x,total)
        return total == x

def main():
    print(is_palindrome(121))


if __name__ == "__main__":
    main()