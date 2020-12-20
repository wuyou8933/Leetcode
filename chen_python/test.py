def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    # reverse
    
    l = 0
    r = len(matrix) -1
    while l < r:
        matrix[l], matrix[r] = matrix[r], matrix[l]
        l += 1
        r -= 1
    # transpose 
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    

matrix =[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(rotate(matrix))