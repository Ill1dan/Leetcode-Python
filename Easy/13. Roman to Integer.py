def romanToInt(s):
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    numbers = []
    temp = []

    for x in s:
        if len(temp) == 0:
            temp.append(x)
        else:
            if roman_values[temp[-1]] <= roman_values[x]:
                temp.append(x)
            else:
                numbers.append(temp)
                temp = [x]

    if len(temp) != 0:
        numbers.append(temp)

    nums = []
    for y in numbers:
        rev = y[::-1]
        temp = []
        print(rev)
        for z in rev:
            if len(temp) == 0:
                temp.append(roman_values[z])
            else:
                if abs(temp[-1]) == roman_values[z]:
                    val = (temp[-1] // roman_values[z]) * roman_values[z]
                    temp.append(val)
                else:
                    temp.append(-roman_values[z])
        nums.append(temp)
        print(temp)

    total = 0

    for i in nums:
        total += sum(i)

    return total

print(romanToInt("DCXXI"))