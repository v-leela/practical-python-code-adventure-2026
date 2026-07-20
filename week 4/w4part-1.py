import math
import requests

url = "https://adventure.practicalpython.org/static/puzzle_input/2026/04/input1.txt"
response = requests.get(url)
lines = response.text.split("\n")
lines.pop()
nrow, ncol = len(lines), len(lines[0])


a, b = nrow, ncol
squares = a + b - math.gcd(a, b)
print(squares)
