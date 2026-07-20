import requests

url = "https://adventure.practicalpython.org/static/puzzle_input/2026/04/input1.txt"
response = requests.get(url)
grid = response.text.split("\n")
grid.pop()
newgrid = [list(line) for line in grid]

#trade for each letter
trade = {
    "L": 199.80,
    "Y": 199.80,
    "Z": 259.30,
    "D": 259.30,
    "G": 299.20,
    "V": 299.20,
    "O": 399.70,
    "T": 399.70,
    "N": 459.90,
    "U": 459.90,
    "A": 599.10,
    "K": 599.10,
    "M": 649.40,
    "C": 649.40,
    "I": 699.00,
    "Q": 699.00,
    "H": 749.70,
    "F": 749.70,
    "J": 799.50,
    "R": 799.50,
    "E": 849.10,
    "X": 849.10,
    "S": 899.40,
    "W": 899.40,
    "P": 899.60,
    "B": 899.60,
}


import math

a, b = len(grid), len(grid[0])

#function for x-coordinate for the line (x/a)+(y/b)=1
def x(y, a, b):
    return a - (a / b) * y


coor = [[1, int(x(1, a, b)) + 1]]
pre = x(1, a, b)

#finding the square coordinates
for i in range(2, b):
    current = x(i, a, b)
    if int(pre) != int(current):
        if pre == int(pre):
            coor.append([i, int(current) + 1])
        else:
            coor.append([i, int(current) + 1])
            coor.append([i, int(current) + 2])
    else:
        coor.append([i, int(current) + 1])

    pre = current
  
coor.append([b, int(x(b, a, b)) + 1])
r_list = []

#evaluating the money from the trade
for lst in coor:
    j = lst[0] - 1
    i = 120 - lst[1]
    letter = newgrid[i][j]

    reward = trade[letter]
    r_list.append(reward)

print(sum(r_list))
