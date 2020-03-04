'''
https://leetcode.com/problems/maximal-square/

'''
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if(m == 0):return 0
        n = len(matrix[0])
        ans =  0
        def f(r,c, m,n, matrix, memo):
            if((r,c) in memo): return memo[(r,c)] 
            if(r in range(m) and c in range(n) and matrix[r][c] == "1"):                
                memo[(r,c)] = 1 + min(f(r,c+1, m,n, matrix, memo), f(r+1,c, m,n, matrix , memo), f(r+1,c+1, m,n, matrix, memo)  )
                return memo[(r,c)]
            return 0 
        memo = {}       
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == "1"):
                    ans = max(ans, f(i,j,m ,n, matrix, memo))
                    
        return ans*ans 