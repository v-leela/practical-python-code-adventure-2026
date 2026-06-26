newpattern = [1, 1, 2, 1, 2]

for i in range(65):
    pattern = newpattern
    pre = None
    count = 1
    newpattern = []

    for a in pattern:
        if pre == a:
            if count + 1 > 2:
                newpattern.append(count)
                newpattern.append(pre)
                count = 1

            else:
                count += 1
        else:
            newpattern.append(count)
            newpattern.append(pre)
            count = 1

        pre = a

    newpattern.append(count)
    newpattern.append(pre)
    newpattern = newpattern[2:]

print(len(newpattern))
