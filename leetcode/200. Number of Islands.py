# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3



def num_islands(arr):

    def dfs(arr, r, c):
        if r > len(arr)-1 or c > len(arr[0])-1 or r<0 or c<0 or arr[r][c] == '0':
            return
        arr[r][c] = '0'
        dfs(arr, r+1, c)
        dfs(arr, r-1, c)
        dfs(arr, r, c+1)
        dfs(arr, r, c-1)

    islands = 0
    if arr is None or len(arr) == 0:
        return islands
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == '1':
                islands += 1
                dfs(arr, r, c)
    return islands

# iterative solution
def numIslands(grid):

    if not grid or len(grid) == 0:
        return 0

    nrows = len(grid)
    ncols = len(grid[0])
    count = 0

    def findneighbors(point):
        r, c = point[0], point[1]
        return [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]

    def findIsland(startPoint):
        q = [startPoint]
        while len(q) > 0:
            p = q.pop(0)
            for r, c in findneighbors(p):
                if 0 <= r < nrows and 0 <= c < ncols and grid[r][c] == '1':
                    grid[r][c] = '0'
                    q.append((r, c))

    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == '1':
                count += 1
                findIsland((i, j))
    return count

if __name__ == '__main__':
    a = [list('11110'), list('11010'), list('11000'), list('00000')]
    print(a, num_islands(a))
