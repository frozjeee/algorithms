def validate_battlefield(field):
    arr = []
    g = [0, 0, 0, 0]
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                arr.append([i, j])
    if len(arr) != 20:
        return False
    for i in range(len(arr)):
        if len(arr) == 0:
            break
        i = arr[0]
        size = 1
        if [i[0], i[1] + 1] in arr:
            while [i[0], i[1] + 1] in arr:
                if [i[0] + 1, i[1] + 1] in arr or [i[0] - 1, i[1] - 1] in arr or [i[0] + 1, i[1] - 1] in arr or [i[0] - 1, i[1] + 1] in arr:
                    return False
                size += 1
                i = arr.index([i[0], i[1] + 1])
                i = arr[i]
                arr.remove([i[0], i[1] - 1])
            if [i[0] + 1, i[1] + 1] in arr or [i[0] - 1, i[1] - 1] in arr or [i[0] + 1, i[1] - 1] in arr or [i[0] - 1, i[1] + 1] in arr:
                return False
            arr.remove([i[0], i[1]])
            if size >= len(g) + 1:
                return False
            else:
                g[size - 1] += 1

        elif [i[0] + 1, i[1]] in arr:
            while [i[0] + 1, i[1]] in arr:
                if [i[0] + 1, i[1] + 1] in arr or [i[0] - 1, i[1] - 1] in arr or [i[0] + 1, i[1] - 1] in arr or [i[0] - 1, i[1] + 1] in arr:
                    return False
                size += 1
                i = arr.index([i[0] + 1, i[1]])
                i = arr[i]
                arr.remove([i[0] - 1, i[1]])
            if [i[0] + 1, i[1] + 1] in arr or [i[0] - 1, i[1] - 1] in arr or [i[0] + 1, i[1] - 1] in arr or [i[0] - 1, i[1] + 1] in arr:
                return False
            arr.remove([i[0], i[1]])
            if size >= len(g) + 1:
                return False
            else:
                g[size - 1] += 1

        else:
            arr.remove([i[0], i[1]])
            if size >= len(g) + 1:
                return False
            else:
                g[size - 1] += 1
    if g == [4, 3, 2, 1]:
        return True

    return False
                

print(validate_battlefield(
    [
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                ]
                ))