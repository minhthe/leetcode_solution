'''
https://leetcode.com/problems/unique-paths-ii/

***approach:
like dp of previous problem, but different these initial i = 0, j = 0 and the obstacle.

***edge case
[[1,0]] -> 1
expect: 0

[[0,0],[1,1],[0,0]] -> 1
expect:  0


***test case:
[[0,0,0],[0,1,0],[0,0,0]]
[[0,0,0],[0,1,0],[0,1,0]]
[[0,0,0]]
[[0]]
[[1,0]]
[[0,0],[1,1],[0,0]]
'''
class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		grid = obstacleGrid
		m = len(grid)
		if m==0: return 0
		n = len(grid[0])
		if n==0: return 0
		if(grid[0][0]==1 or grid[m-1][n-1] == 1): return 0
		rst = [[0 for i in range(n)] for j in range(m)]
		row  = False
		col = False
		for i in range(m):
			for j in range(n):
				if(grid[i][j]== 1):
					rst[i][j] = 0
					if i == 0: row = True
					if j == 0: col = True
				elif(i == 0 and row == False ):
					rst[i][j] = 1 
				elif(j == 0 and col == False ):
					rst[i][j] = 1 
				else:
					rst[i][j] = rst[i-1][j] + rst[i][j-1]
		return rst[m-1][n-1]