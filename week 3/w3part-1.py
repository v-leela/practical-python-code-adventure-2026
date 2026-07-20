import requests

url = "https://adventure.practicalpython.org/static/puzzle_input/2026/03/input1.txt"
response = requests.get(url)
thelist = response.text.split("\n")
thelist.pop()
str_unsort = []
for line in thelist:
    num = "".join([st for st in line if st != " " and st != "-"])
    if num != "":
        str_unsort.append(num)

incom = list(map(int, str_unsort))


#algorithm for finding the no.of flips

flip = 0

while len(incom) > 1:
    if incom == sorted(incom):
        break

    elif incom[-1] == max(incom):
        incom = incom[:-1]

    elif incom[0] != max(incom):
        flip += 2
        idx = incom.index(max(incom))
        incom = incom[: idx + 1][::-1] + incom[idx + 1 :]
        incom = incom[::-1][:-1]

    elif incom[0] == max(incom):
        incom = incom[1:][::-1]
        flip += 1

print(flip)
