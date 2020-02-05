'''
https://leetcode.com/problems/unique-paths-iii/

'''
def	dfs(grid, visited, rst, start , end, cnt_condition, m , n, dx, dy):
	cnt = 0 
	if(cnt_condition == -1 and start[0] == end[0] and start[1] == end[1]):
		return 1 
	for i in range(4):
		x , y = dx[i] + start[0], dy[i] + start[1]
		if(x in range(m) and y in range(n) and grid[x][y]!= -1 and visited[x][y] == False):
			visited[x][y] = True
			cnt += dfs(grid, visited, rst, (x, y) , end, cnt_condition -1 , m , n, dx, dy)
			visited[x][y] = False
	return cnt
			
class Solution(object):
	def uniquePathsIII(self, grid):
		m = len(grid)
		if m == 0 : return 0
		n = len(grid[0])
		if n == 0 : return 0 
		cnt_condition, start, end = 0 , (-1, -1), (-1, -1)
		for i in range(m):
			for j in range(n):
				if(grid[i][j] == 0): cnt_condition += 1 
				elif(grid[i][j] == 1): start = (i, j)
				elif(grid[i][j] == 2): end = (i,j)
		if(start[0] == -1 or end[0] == -1): return 0
		rst = []
		visited = [[False for i in range(n)] for j in range(m)]
		dx, dy  = [-1, 1, 0 , 0], [0 ,0 , -1, 1]
		visited[start[0]][start[1]] = True
		return dfs(grid, visited, rst, start , end, cnt_condition, m , n, dx, dy)	