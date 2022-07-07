#    7  1  5  3  6  4
# 7  x -6 -2 -4 -1 -3
# 1  x  x  4  2  5  3
# 5  x  x  x -2  1 -1
# 3  x  x  x  x  3  1
# 6  x  x  x  x  x -2
# 4  x  x  x  x  x  x

#    2  1  2  1  0  1  2
# 2  x -1  0 -1 -2 -1  0
# 1  x  x  1  0 -1  0  1
# 2  x  x  x -1 -2 -1  0
# 1  x  x  x  x -1  0  1
# 0  x  x  x  x  x  1  2
# 1  x  x  x  x  x  x  1
# 2  x  x  x  x  x  x  x

#    1  9  0  5
# 1  x  8 -1  4
# 9  x  x -9 -4
# 0  x  x  x  5
# 5  x  x  x  x

def solve(arr):
    l = 0
    r = 1
    maxProf = 0
    while r < len(arr):
        current = arr[r] - arr[l]
        if arr[l] < arr[r]:
            maxProf = max(current, maxProf)
        else:
            l = r
        r += 1
    return maxProf

print(solve([2,1,2,1,0,1,2])) 