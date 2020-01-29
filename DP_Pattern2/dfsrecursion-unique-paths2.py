'''
https://leetcode.com/problems/unique-paths
Using DFS Recursion + memo to AC

***next level:
https://leetcode.com/problems/unique-paths-ii/

'''
def dfs(i,j, m,n, memo):
    if(i == m -1 and j == n-1):
        return 1
    if (i,j) in memo:
        return memo[(i,j)]
    if(i in range(m) and j in range(n)):
        memo[(i,j)] =  dfs(i+1,j, m, n, memo) + dfs(i, j+1, m, n, memo) 
        return  memo[(i,j)]
    
    else:
        return 0
class Solution(object):
    def uniquePaths(self, m, n):
        if m ==0 or n ==0 : return 0
        memo = {}
        cnt = 0 
        i, j = 0 ,0
        return dfs(i,j, m,n, memo)
        