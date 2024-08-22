def findComplement(num):

    def binary(num):
        res = 0
        multiplier = 1

        while num > 0:
            res += (num % 2) * multiplier
            num //= 2
            multiplier *= 10

        return res

    def complement(num):
        num = str(num)
        res = ""

        for i in num:
            if i == "1":
                res += "0"
            else:
                res += "1"

        return int(res)

    def decimal(num):
        res = 0
        power = 0

        while num > 0:
            res += (num % 10) * (2 ** power)
            num //= 10
            power += 1

        return res

    binary_num = binary(num)
    complementary_num = complement(binary_num)
    res = decimal(complementary_num)

    return res


num = 5
print(findComplement(num))