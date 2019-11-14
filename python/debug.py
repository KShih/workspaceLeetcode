class Solution:
    def updateMatrix(self, matrix):
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        def distance(i, j, count, min_dis):
            if matrix[i][j] == 0:
                return count

            for k in range(len(direction)):
                x, y = i+direction[k][0], j+direction[k][1]
                if 0 <= x < r and 0 <= y < c:
                    if count + 1 < min_dis:
                        min_dis = min(min_dis, distance(x, y, count+1, min_dis))

            return min_dis


        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    matrix[i][j] = distance(i,j, 0, 201)

        return matrix

if __name__ == '__main__':
    s = Solution()
    print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
