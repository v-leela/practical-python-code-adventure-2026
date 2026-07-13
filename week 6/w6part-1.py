import requests
import matplotlib.pyplot as plt

url = "https://adventure.practicalpython.org/static/puzzle_input/2026/06/input1.txt"
response = requests.get(url)
puzzle_input = response.text.split("\n")
puzzle_input.pop()

all_points = []
for c in puzzle_input:
    all_points.append(tuple(map(int, c.split(","))))


###function for convexity checking
def check_covexity(p1, p2, other_points):
    x1, y1 = p1
    x2, y2 = p2
    slist = set()
    for point in other_points:
        xp, yp = point
        value = (yp - y1) * (x2 - x1) - (y2 - y1) * (xp - x1)
        sign = (value > 0) - (value < 0)
        slist.add(sign)
        if 1 in slist and -1 in slist:
            return True  # p2 is collinear with the line formed by p1 and p3.

    return False  # p2 is not collinear with the line formed by p1 and p3.


###first loop
all_points = sorted(all_points)
starting_point = all_points[0]
all_points.pop(0)
coordinates = sorted([p for p in all_points if p != starting_point])
vertices = [starting_point]

count = 0
for p in all_points:
    last_vertex = vertices[-1]
    if not check_covexity(last_vertex, p, coordinates):
        vertices.append(p)
        coordinates.remove(p)
    count += 1
    # print(count)

all_points.append(vertices[0])
vertices.pop(0)  # the "starting_point" won't be a good starting point.


###second loop
rall_points = [p for p in sorted(all_points, reverse=True) if p[1] > 7281]
starting_point = rall_points[0]
rall_points.pop(0)
coordinates = sorted([p for p in rall_points if p != starting_point])

for p in rall_points:
    last_vertex = vertices[-1]
    if not check_covexity(last_vertex, p, coordinates):
        vertices.append(p)
        coordinates.remove(p)

    count += 1
    # print(count)

# print(len(vertices))
# print(vertices)


###function for collinearity check
def coll_check(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    value = (y3 - y1) * (x2 - x1) - (y2 - y1) * (x3 - x1)
    return value


###third loop for coll_check

current = None
last = vertices[-1]

while current != last:
    copy_ofvertices = vertices.copy()

    for idx in range(len(vertices)):
        current = vertices[idx]

        p1 = vertices[idx]
        p2 = vertices[(idx + 1) % len(vertices)]
        p3 = vertices[(idx + 2) % len(vertices)]

        if coll_check(p1, p2, p3) == 0:
            copy_ofvertices.remove(p2)
            vertices = copy_ofvertices
            count += 1
            break


# print(vertices)


###ploting
x = [p[0] for p in vertices]
y = [p[1] for p in vertices]
lst = [x for x in all_points if x not in vertices]
xo = [p[0] for p in lst]
yo = [p[1] for p in lst]

plt.figure(figsize=(6, 6))
plt.plot(x + [x[0]], y + [y[0]], color="red", linewidth=2)
plt.scatter(x, y, color="red", s=40, zorder=3)
plt.scatter(xo, yo, color="blue", alpha=0.1)

plt.xlabel("x")
plt.ylabel("y")
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.grid(True)
plt.axis("equal")
plt.show()


###answer
final_price = (len(vertices)) * (len(all_points))
print(f"the final cost to build the barrier is ⅊ {final_price}.")
