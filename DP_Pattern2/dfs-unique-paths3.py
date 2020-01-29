'''
https://leetcode.com/problems/unique-paths/

'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        rst = [[0 for i in range(n)] for j in range(m)]
        rst[0][0] = 1
        for i in range(m):
            for j in range(n):
                if(i == 0 or j == 0):
                    rst[i][j] = 1
                else:
                    rst[i][j] = rst[i][j-1] +rst[i-1][j]
        return rst[m-1][n-1]
         