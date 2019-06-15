from collections import deque

WALL = -1
GATE = 0
EMPTY = 2147483647


def wallsAndGates(rooms):
    """
    Do not return anything, modify rooms in-place instead.
    """
    m = len(rooms) - 1
    n = len(rooms[0]) - 1

    def findNeighbors(point):
        x = point[0]
        y = point[1]
        return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]

    def findDistanceToGate(r, c):
        disntances = [[0] * n] * m
        print('size of distances =', m, n)
        q = deque()
        q.append((r, c))
        while len(q) > 0:
            p = q.popleft()
            for point in findNeighbors(p):
                x = point[0]
                y = point[1]
                if x < 0 or y < 0 or x > m or y > n or rooms[x][y] == WALL or disntances[x][y] != 0:
                    pass
                else:
                    disntances[x][y] += 1
                    if rooms[x][y] == GATE:
                        return disntances[x][y]
                    q.append(point)
        return EMPTY

    for i in range(m + 1):
        for j in range(n + 1):
            if rooms[i][j] == EMPTY:
                rooms[i][j] = findDistanceToGate(i, j)



if __name__ == '__main__':
    input = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

    print(wallsAndGates(input))