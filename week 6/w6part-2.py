import requests
import matplotlib.pyplot as plt

url = "https://adventure.practicalpython.org/static/puzzle_input/2026/06/input2.txt"
response = requests.get(url)
puzzle_input = response.text.split("\n")
puzzle_input.pop()
all_points = [tuple(p.split(",")) for p in puzzle_input]
all_points = [[tuple(map(int, [p[0], p[1]])), p[2]] for p in all_points]
not_U = [p for p in all_points if p[1] != "U"]


###function for convexity checking
def check_covexity(p1, p2, other_points):
    x1, y1 = p1[0]
    x2, y2 = p2[0]
    slist = set()
    for point in other_points:
        xp, yp = point[0]
        value = (yp - y1) * (x2 - x1) - (y2 - y1) * (xp - x1)
        sign = (value > 0) - (value < 0)
        slist.add(sign)
        if 1 in slist and -1 in slist:
            return False
    return True


###first loop
starting_point = min(not_U)
not_U1 = [p for p in sorted(not_U) if p[0][1] < starting_point[0][1]]
vertices = [starting_point]

for p in not_U1:
    last_vertex = vertices[-1]
    if check_covexity(last_vertex, p, not_U):
        vertices.append(p)
        not_U.remove(p)

not_U1.append(vertices[0])
print(vertices)



###second loop
rnot_U = [p for p in sorted(not_U, reverse=True) if p[0][1] > vertices[-1][0][1]]
starting_point = rnot_U[0]
rnot_U.pop(0)

for p in rnot_U:
    last_vertex = vertices[-1]
    if check_covexity(last_vertex, p, not_U):
        vertices.append(p)
        not_U.remove(p)

print(len(vertices))
print(vertices)



###function for collinearity check
def coll_check(p1, p2, p3):
    x1, y1 = p1[0]
    x2, y2 = p2[0]
    x3, y3 = p3[0]
    value = (y3 - y1) * (x2 - x1) - (y2 - y1) * (x3 - x1)
    if not value:
        return True  # p2 is coll with the line joining the points p1 and p3
    return False  # p2 is not coll with the line joining the points p1 and p3



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

        if coll_check(p1, p2, p3):
            copy_ofvertices.remove(p2)
            vertices = copy_ofvertices
            count += 1
            break

print("=" * 40)
print(f"final vertices ---> {vertices}")
print("=" * 40)



###counting all the points in the convex hull
num_inhull = 0
rpoint = not_U[67]  # chose a random point inside the hull(we know the points which are not "U" will be inside the convex hull)
for point in sorted(all_points):
    sum_of_bool = sum(
        [
            check_covexity(
                vertices[i], vertices[(i + 1) % len(vertices)], [point, rpoint]
            )
            for i in range(len(vertices))
        ]
    )
    if sum_of_bool == len(vertices):
        num_inhull += 1

print(num_inhull)



###ploting
x = [p[0][0] for p in vertices]
y = [p[0][1] for p in vertices]
lst = [x for x in all_points if x not in vertices]
xo = [p[0][0] for p in lst]
yo = [p[0][1] for p in lst]
xnu = [p[0][0] for p in not_U]
ynu = [p[0][1] for p in not_U]

plt.figure(figsize=(6, 6))
plt.plot(x + [x[0]], y + [y[0]], color="red", linewidth=2)
plt.scatter(x, y, color="red")
plt.scatter(xnu, ynu, color="blue", alpha=0.3)
plt.scatter(xo, yo, color="grey", alpha=0.08)

plt.xlabel("x")
plt.ylabel("y")
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.grid(True)
plt.axis("equal")
plt.show()


###answer
final_price = (len(vertices)) * (num_inhull)
print(f"the final cost to build the barrier is ⅊ {final_price}.")
