newpattern = list("12111112121112111212212112111212")
newpattern = list(map(int, newpattern))

for i in range(65):
    pattern = newpattern
    pre = 0
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

