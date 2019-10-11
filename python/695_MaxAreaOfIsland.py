class Solution(object):
    def maxAreaOfIsland(self, grid):
        def findIsland(i, j, count):
            if grid[i][j] != 1:
                return count
            else:
                count += 1
                grid[i][j] *= -1
                for k in range(4):
                    if 0 <= i+dx[k] < col and 0 <= j+dy[k] < row:
                        count = findIsland(i+dx[k], j+dy[k], count)
                return count


        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        row, col = len(grid[0]), len(grid)

        maxCount = 0
        for i in range(col):
            for j in range(row):
                if grid[i][j] == 1:
                    maxCount = max(maxCount, findIsland(i,j,0))
        return maxCount

if __name__ == "__main__":
    s = Solution()
    print(s.maxAreaOfIsland([
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
