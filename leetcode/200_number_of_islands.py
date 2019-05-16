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

if __name__ == '__main__':
    a = [list('11110'), list('11010'), list('11000'), list('00000')]
    print(a, num_islands(a))
