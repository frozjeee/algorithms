def editDistance(s1, s2):
    matrix = []
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    matrix.append(distances)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        matrix.append(distances_)
        distances = distances_
    return [matrix, s1, s2]
        

def outputAlignment(i, j, matrix, s1, s2, a):
    if i == j == 0:
        return
    if i > 0 and matrix[i][j] == matrix[i - 1][j] + 1:  
        outputAlignment(i - 1, j, matrix, s1, s2, a)
        a.append(["-", s1[i]])
    elif j > 0 and matrix[i][j] == matrix[i][j - 1] + 1:
        outputAlignment(i, j - 1, matrix, s1, s2, a)
        a.append([s2[j], "-"])
    else:
        outputAlignment(i - 1, j - 1, matrix, s1, s2, a)
        a.append([s2[j], s1[i]])
    return a


output = editDistance("bread", "really")
a = []
print(output[0])
s = outputAlignment(len(output[0]) - 1, len(output[0][0]) - 1, output[0], f" {output[2]}", f" {output[1]}", a)
print('--')
print(s)
