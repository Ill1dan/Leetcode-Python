def isPalindrome(x):
    num1 = x
    num2 = 0

    if num1 < 0:
        return False

    while num1 > 0:
        num2 = (num2 * 10) + (num1 % 10)
        num1 = num1 // 10

    return x == num2

print(isPalindrome(121))
