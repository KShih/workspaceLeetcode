class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        res, heights = 0, [0 for _ in range(col)]

        for i in range(row):
            for j in range(col):
                heights[j] = (1+heights[j]) if matrix[i][j] != '0' else 0
            res = max(res, self.largestRectangleArea(heights))
        return res

    def largestRectangleArea(self, heights):
        # [3, 1, 3, 2, 2]
        heights = list(map(int, heights))
        max_a = 0
        stack = [-1]
        heights.append(0)
        for i in range(len(heights)):
            if heights[i] < heights[stack[-1]]:
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_a = max(max_a, h*w)
            stack.append(i)
        return max_a


if __name__ == '__main__':
    s = Solution()
    matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
    print(s.maximalRectangle(matrix))
