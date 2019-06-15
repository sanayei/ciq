import collections
WALL = -1
GATE = 0
EMPTY = 2147483647


def wallsAndGates(rooms):
    """
    Do not return anything, modify rooms in-place instead.
    """
    if not rooms or len(rooms) == 0:
        return
    nrows = len(rooms)
    ncols = len(rooms[0])

    def findNeighbors(point):
        x = point[0]
        y = point[1]
        return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]

    q = collections.deque()
    for i in range(nrows):
        for j in range(ncols):
            if rooms[i][j] == GATE:
                q.append((i, j))

    while len(q) > 0:
        p = q.popleft()
        for r, c in findNeighbors(p):
            if 0 <= r < nrows and 0 <= c < ncols and rooms[r][c] == EMPTY:
                rooms[r][c] = rooms[p[0]][p[1]] + 1
                q.append((r, c))
    return rooms

if __name__ == '__main__':


    rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

    print(wallsAndGates(rooms))



