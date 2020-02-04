'''
https://leetcode.com/problems/unique-paths-ii/
'''
def dfs(grid, m ,n ,i , j , memo):
	if(i in range(m) and j in range(n) and grid[i][j] == 1):
		memo[(i,j)] = 0
		return 0
	elif( (i,j) in memo ):
		return memo[(i,j)]
	elif( i == m -1 and j == n -1):
		memo[(i,j)] = 1 
		return 1	
	elif i in range(m) and j in range(n):
		memo[(i,j)] = dfs(grid, m ,n ,i + 1, j , memo) + dfs(grid, m ,n ,i , j +1 , memo)
		return memo[(i,j)]
	else:
		return 0
class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		grid =  obstacleGrid
		m = len(grid)
		if m == 0 : return 0
		n = len(grid[0])
		if n ==0: return 0
		rst = [[0 for i in range(n)]for j in range(m)]
		memo = {}
		i , j = 0 , 0
		dfs(grid, m, n ,i , j , memo)
		return memo[(i ,j)]