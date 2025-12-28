def helper(matrix, coord, idx, value, n):

    if value == n*n + 1:
        return matrix

    i, j = coord
    matrix[i][j] = value

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
 
    dx, dy = direction[idx]
    next_i, next_j = i + dx, j + dy
    
    if not (0 <= next_i < n and 0 <= next_j < n and matrix[next_i][next_j] == 0):
        idx = (idx + 1) % 4
        dx, dy = direction[idx]
        next_i, next_j = i + dx, j + dy
    
    return helper(matrix, (next_i, next_j), idx, value + 1 ,n)


def spiralMatrix(n):
    
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    coord = (0, 0)
    answer = helper(matrix, coord, 0, 1, n)

    print(answer)    

spiralMatrix(5)