def vertical_symmetry(arr):
    if len(arr) % 2 == 1:
        d = len(arr) / 2 + 0.5
    else:
        d = len(arr) / 2
    j = -1
    a = False
    for i in range(len(arr)):
        for q in range(0, int(d)):
            if arr[i][q] != arr[i][j]:
                a = True
                break
            j -= 1
        j = -1
    return 'не Симметрично по вертикали' if a else ' Симметрично по вертикали'


def diagonal_symmetry(arr):
    if len(arr) != len(arr[0]):
        return 'Для данной фигуры нельзя просчитать данную метрику'
    else:
        h = ''
        n, k = len(arr), len(arr[0])
        for k in range(n - 1):
            for l in range(k + 1, n):
                if arr[k][l] != arr[l][k]:
                    h = ('False')
                    break
        if h != ('False'):
            return 'По диагонали есть симметрия'
        else:
            return 'По диагонали нет симметрии'


def horizontal_symmetry(arr):
    if len(arr) % 2 == 1:
        d = len(arr) / 2 + 0.5
    else:
        d = len(arr) / 2
    a = None
    j = -1
    for i in range(int(d)):
        if arr[i] == arr[j]:
            pass
        else:
            a = 'По горизонтали нет симметрии'
            break
        j -= 1
    return a if a else 'По горизонтали есть симметрия'


arr = [[1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1]]

print(vertical_symmetry(arr),
      diagonal_symmetry(arr),
      horizontal_symmetry(arr))
