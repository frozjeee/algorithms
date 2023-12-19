def partitionLabels(s):
    dct ={}
    ret = []

    for i in range(len(s)):
        if s[i] not in dct:
            dct[s[i]] = [i, i]
        else:
            dct[s[i]].pop()
            dct[s[i]].append(i)

    min_v = dct[s[0]][0]
    max_v = dct[s[0]][1]
    for i in list(dct.values())[1:]:
        print(i, min_v, max_v)
        if i[0] > max_v:
            print("WASD")
            ret.append(max_v - min_v + 1)
            max_v = i[1]
            min_v = i[0]

        elif i[1] > max_v:
            max_v = i[1]
    ret.append(max_v - min_v + 1)
    print(ret)


partitionLabels("eccbbbbdec")