stack = """ 127-
  -
-154-
128--
   -7
97
 - -
-54
--73
-   -
-105-
--22
-----
-59
-   -
30--
  5--
107-
-   -
-26

96-
-   -
-156-
-- --
- - -
140
-   -
12-
-   -
-   -
 32--
38-

-   -
 135-
-47
-- --
- - -
62-
--15
-   -
-   -
-126-
9--
   -8
-56-
63-
-48
-   -
-82
-66

 152-
  -
151-
  -41
-142
-   -
--165
  95
57
--58-
99--
-   -
-112-
-   -
-102
  137
-145
-143
 158-
-   -
  -

  -11
  --
-86
24-
 -  -
  60-
-104
  88-
-136-
50-
93
-116
 83-
 -
   -
 78--
106-
-   -
 ---
--144
 --91
--23-
-111

  -
--77-
-81
--121
138
 - -
-   -
 -139
-120
-----
98--
-   -
 155-
-   -
67-
-167
-80-
-141
-108-
 85-
134
70--

119-
-129
-36
-   -
-92-
69--
-   -
168-
-   -
-   -
130
-   -
169
 ---
--160
  74
146-
132

72
-161-
 94-
--34-
-115
----
-123
-   -
  -40
-76
--28
21-
--10
-   -
 -101
79-
25--
-162
113-
---
-  -
52
 -39-
-35
--133
-   -
--27-

-   -
 122-
-   -
-   -
166-
-19
51-
 131-
149-
-   -
-55
-   -
29--
  163
-13
-125-
 ---
--17

6-
-33-
  --
 -68-
42--
-37
 -  -
 100--
103--
53-
--45-
 -
87-
--31-
-49
-148
--90
   -
-71
-   -
75-
 109
150-
43
 -89-
164-
84-
-46-
124
 -16-
 ---"""

#converting the stack into useful incomplete(incom) and logical(logi) lists

thelist = stack.split(sep="\n")
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
