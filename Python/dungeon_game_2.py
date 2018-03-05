def dungeon(m,n):
    result = [[0]*(n) for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i+j>=n:
                break
            result[m-i-1][i+j]=1
    print result

    for i in range(0,m):
        for j in range(1,n):
            if i+j>=n:
                break
            result[m - i - 1][j + i] = result[m - i - 1][j + i - 1]
            if (i > 0):
                result[m - i - 1][j + i] += result[m - i][j + i - 1]
            if (i < m - 1):
                result[m - i - 1][j + i] += result[m - i - 2][j + i - 1]

    return result[m-1][n-1]

print dungeon(3,4)