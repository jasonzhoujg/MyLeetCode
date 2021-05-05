class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0 for i in range(n)] for i in range(m)]

        for i in range(m):
            if obstacleGrid[i][0]==1:break
            res[i][0]=1
        for j in range(n):
            if obstacleGrid[0][j]==1:break
            res[0][j]=1
        

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]==1:continue
                res[i][j] = res[i - 1][j] + res[i][j - 1]

        return res[m-1][n-1]
