class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for i in range(n)] for j in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if j==0:res[i][0]= 1
                elif i == 0: res[0][j]=1
                else:res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[m-1][n-1]
