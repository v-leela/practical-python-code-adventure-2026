import requests
import random

url = "https://adventure.practicalpython.org/static/puzzle_input/2026/05/input2.txt"
response = requests.get(url)
puzzle_input = response.text.split("\n")
puzzle_input.pop()
grid = [list(line) for line in puzzle_input]


for i, line in enumerate(grid):
    if "@" in line:
        start = line.index("@")
        break


path = [[i, start]]
visited = [[i, start]]


def get_neighbours(i, j):
    neighbours = []
    if grid[i][j - 1] == "0" and [i, j - 1] not in visited:
        # left
        neighbours.append([i, j - 1])
    if grid[i][j + 1] == "0" and [i, j + 1] not in visited:
        # right
        neighbours.append([i, j + 1])
    if grid[i - 1][j] == "0" and [i - 1, j] not in visited:
        # up
        neighbours.append([i - 1, j])
    if grid[i + 1][j] == "0" and [i + 1, j] not in visited:
        # down
        neighbours.append([i + 1, j])
    if grid[i - 1][j - 1] == "0" and [i - 1, j - 1] not in visited:
        # diagonal1
        neighbours.append([i - 1, j - 1])
    if grid[i - 1][j + 1] == "0" and [i - 1, j + 1] not in visited:
        # diagonal2
        neighbours.append([i - 1, j + 1])
    if grid[i + 1][j - 1] == "0" and [i + 1, j - 1] not in visited:
        # diagonal3
        neighbours.append([i + 1, j - 1])
    if grid[i + 1][j + 1] == "0" and [i + 1, j + 1] not in visited:
        # diagonal4
        neighbours.append([i + 1, j + 1])

    return neighbours


row, col = i, start
old_row, old_col = None, None

while not ([row, col] == [i, start] and [old_row, old_col] != [None, None]):
    neighbours = get_neighbours(row, col)

    if neighbours:
        old_row, old_col = row, col
        row, col = random.choice(neighbours)
        visited.append([row, col])
        path.append([row, col])
    else:
        row, col = path[-2]
        path.pop()


print(len(visited))
