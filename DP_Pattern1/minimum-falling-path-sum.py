'''
https://leetcode.com/problems/minimum-falling-path-sum/

AC when 40 minutes

Time and space complexity: O(r*c)
'''
class Solution(object):
    def minFallingPathSum(self, A):
        r  =len(A)
        if r==0 : return 0 
        c = len(A[0])
        if c==0 : return 0
        k = [[0 for i in range(c)] for j in range(r)]
        
        for i in range(r):
            for j in range(c):
                if i == 0:
                    k[i][j] = A[i][j]
                else:
                    if(j ==0 ):
                        k[i][j] = min( k[i-1][0], k[i-1][1] ) + A[i][j]
                    elif(j == c-1 ):
                        k[i][j] = min( k[i-1][c-1], k[i-1][c-2] ) + A[i][j]
                    else:
                        k[i][j] = min(k[i-1][j-1],k[i-1][j], k[i-1][j+1])    + A[i][j]  
                        
        return min(k[r-1])