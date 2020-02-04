'''
https://leetcode.com/problems/unique-paths/

after debug :try to learn after:
def handle(m ,n , row, col , rst):
    if(row >= m or col >= m):
        return 0 
    if(rst[row][col] != 0):
        return rst[row][col]
    if(m-1 == row and n - 1 == col):
        return 1 
    row_count = handle(m ,n , row + 1, col, rst)
    col_count = handle(m ,n , row , col+1, rst)
    rst[row][col] = row_count + col_count
    return rst[row][col]
if __name__ == '__main__':
    m , n = 3 ,3 
    rst = [[0 for i in range(3)] for j in range(3)]
    print(handle(m, n , 0 ,0 , rst))
    
    
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
         