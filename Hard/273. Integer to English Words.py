def numberToWords(num):
    if num == 0:
        return "Zero"

    ones_map = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen"
    }

    tens_map = {
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety"
    }

    def each_string(n):
        three_string = []

        hundred = n // 100
        if hundred:
            three_string.append(ones_map[hundred] + " Hundred")

        tens = n % 100
        if tens >= 20:
            ten, one = tens // 10, tens % 10
            three_string.append(tens_map[ten * 10])
            if one:
                three_string.append(ones_map[one])
        elif tens:
            three_string.append(ones_map[tens])

        return " ".join(three_string)

    postfix = ["", " Thousand", " Million", " Billion"]
    i = 0
    res = []

    while num:
        digits = num % 1000
        s = each_string(digits)
        if s:
            res.append(s + postfix[i])
        num = num // 1000
        i += 1

    res.reverse()
    return " ".join(res)


num = 1234567
print(numberToWords(num))