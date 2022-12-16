def func(n):
    z = []
    a = {}
    for i in range(10):
        for j in range(10):
            a[(i, j)] = 0
            for q in range(len(n)):
                a2 = []
                if (i * n[q][3] - n[q][1] + j) * (i * n[q][0] - n[q][2] + j) == 0:
                    a2.append(1)
                else:
                    a2.append(0)
                a[(i, j)] += sum(a2)

    a1 = None
    for x, y in a.items():
        if a1 is None:
            a1 = x
        else:
            if a[a1] < y:
                a1 = x
    return a1[0], a1[1]


print(func([[0, 0, 0, 1], [1, 0, 1, -1], [2, 0, 2, 1], [3, 0, 3, -1], [5, 5, 10, 10]]))
