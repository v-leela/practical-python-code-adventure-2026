newpattern = list("12111112121112111212212112111212")
for i in range(65):
    pattern = list(map(int, newpattern))
    pre = 0
    count = 1
    newpattern = []

    for a in pattern:
        if pre == a:
            if count + 1 > 2:
                newpattern.append(str(count))
                newpattern.append(str(pre))
                count = 1
                """ if i == 64:
                    three_count += 1 """

            else:
                count += 1
        else:
            newpattern.append(str(count))
            newpattern.append(str(pre))
            count = 1

        pre = a

    newpattern.append(str(count))
    newpattern.append(str(pre))
    newpattern = newpattern[2:]

t3 = 0
numcount = 1
pre = 0
for a in newpattern:
    if pre == a:
        numcount += 1
    else:
        numcount = 1

    if numcount == 3:
        t3 += 1
    pre = a

print(t3)

