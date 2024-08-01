def countSeniors(details):
    res = 0
    for i in details:
        age = int(i[11:13])
        if age > 60:
            res += 1

    return res


details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
print(countSeniors(details))