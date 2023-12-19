def MinMax(i, j, op, m, M):
    mmin = float("inf")
    mmax = float("-inf")
    for k in range(i, j):
        a = eval(f"{M[i][k]} {op[k]} {M[k+1][j]}")
        b = eval(f"{M[i][k]} {op[k]} {m[k+1][j]}")
        c = eval(f"{m[i][k]} {op[k]} {M[k+1][j]}")
        d = eval(f"{m[i][k]} {op[k]} {m[k+1][j]}")
        mmin = min(mmin, a, b, c, d)
        mmax = max(mmax, a, b, c, d)
    return(mmin, mmax)


# O(n^3) 
def get_maximum_value(dataset):
    op = dataset[1:len(dataset):2]
    d = dataset[0:len(dataset)+1:2]
    n = len(d)
    m = [[0 for _ in range(n)] for _ in range(n)]  #minimized values
    M = [[0 for _ in range(n)] for _ in range(n)]  #maximized values
    for i in range(n):
        m[i][i] = int(d[i])   #so that the tables will look like
        M[i][i] = int(d[i])   #[[i, 0, 0...], [0, i, 0...], [0, 0, i,...]]
    for s in range(1, n):  
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = MinMax(i,j,op,m,M) 
    return M[0][n-1]

print(get_maximum_value([5,"+", 8, "-", 3]))