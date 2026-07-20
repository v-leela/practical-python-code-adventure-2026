import requests

url = "https://adventure.practicalpython.org/static/puzzle_input/2026/03/input1.txt"
response = requests.get(url)
thelist = response.text.split("\n")
thelist.pop()
str_unsort = []
indices = []
numbers = []

for line in thelist:
    num = "".join([st for st in line if st != " " and st != "-"])
    if num != "":
        str_unsort.append(num)
        frst = num[0]
        idx = line.index(frst)
        indices.append(idx)
        numbers.append(line)

incom = list(map(int, str_unsort))
logi = []

for i in range(len(numbers)):
    if indices[i] != 0:
        if numbers[i][indices[i] - 1] == "-":
            logi.append(-1)
        else:
            logi.append(1)
    else:
        logi.append(1)


#algorithm for finding no.of flips

flip = 0

while len(incom) > 1:
  
    if incom == sorted(incom) and logi == [1] * len(logi):
        break

    elif incom[-1] == max(incom):
        if logi[-1] != 1:
            flip += 3
        incom = incom[:-1]
        logi = logi[:-1]

    elif incom[0] != max(incom):
        idx = incom.index(max(incom))
        if logi[idx] == -1:
            flip += 3
        else:
            flip += 2
        logi = [lg if i < idx else -lg for i, lg in enumerate(logi)]
        incom = incom[: idx + 1][::-1] + incom[idx + 1 :]
        incom = incom[::-1][:-1]
        logi = logi[: idx + 1][::-1] + logi[idx + 1 :]
        logi = logi[::-1][:-1]

    elif incom[0] == max(incom):
        if logi[0] == 1:
            flip += 2
        else:
            flip += 1
        logi = [-lg for lg in logi]
        incom = incom[1:][::-1]
        logi = logi[1:][::-1]

print(flip)
