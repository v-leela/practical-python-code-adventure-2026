import requests
from collections import Counter

url = "https://adventure.practicalpython.org/static/puzzle_input/2026/05/input1.txt"
response = requests.get(url)
puzzle_input = response.text.split("\n")
wall = [list(line) for line in puzzle_input]
wall = [list(map(int, wall_line)) for wall_line in wall]


coordinates = []
for i, row in enumerate(wall):
    for j, type in enumerate(row):
        if type == 7:
            coordinates.append([i, j])


order = ("up", "left", "down", "right")
wall_types = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
]


true_type = []


for c in coordinates:
    i, j = c
    cwall_type = [0, 0, 0, 0]

    if wall[i][j - 1] != 0:
        # left
        if wall_types[wall[i][j - 1]][3] == 1:
            cwall_type[1] = 1
    if wall[i][j + 1] != 0:
        # right
        if wall_types[wall[i][j + 1]][1] == 1:
            cwall_type[3] = 1
    if wall[i - 1][j] != 0:
        # up
        if wall_types[wall[i - 1][j]][2] == 1:
            cwall_type[0] = 1
    if wall[i + 1][j] != 0:
        # down
        if wall_types[wall[i + 1][j]][0] == 1:
            cwall_type[2] = 1

    true_type.append(wall_types.index(cwall_type))


print(dict(sorted(Counter(true_type).items())))
print("".join([str(value) for key, value in sorted(Counter(true_type).items())]))
