class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        visited = [False for _ in range(n)]
        count = 0
        for i in range(n):
            if visited[i] == True:
                continue
            self.dfs(M, visited, i)
            count += 1
        return count

    def dfs(self, M, visited, i):
        visited[i] = True
        for k in range(len(M)):
            if M[i][k] != 1 and visited[k] == True:
                continue
            self.dfs(M, i, visited)


if __name__ == "__main__":
    x = Solution()
    print(x.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
