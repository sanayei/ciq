from collections import deque


def updateMatrix(matrix):
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix

    nrows = len(matrix)
    ncols = len(matrix[0])
    dist = [[0] * ncols for i in range(nrows)]

    def findNeighbors(r, c):
        return [(r, c + 1), (r + 1, c), (r - 1, c), (r, c - 1)]

    q = deque()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                q.append((i, j))


    while len(q) > 0:
        x, y = q.popleft()
        for r, c in findNeighbors(x, y):
            if 0 <= r < nrows and 0 <= c < ncols and matrix[r][c] == 1:
                dist[r][c] = dist[x][y] + 1
                q.append((r, c))


if __name__ == '__main__':
    m =[[0,0,0],[0,1,0],[1,1,1]]
    print(updateMatrix(m))