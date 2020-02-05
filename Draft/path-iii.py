def dfs(visited, grid, pos_start, pos_end, cnt_condition, cnt_obstacle, rst,dx, dy, m ,n):
	if(cnt_condition == -1 and pos_start[0] == pos_end[0] and pos_start[1] == pos_end[1]):
		print('herer')
		rst.append(1)
		return 
	for i in range(4):
		x, y = dx[i] + pos_start[0], dy[i] + pos_start[1]
		if(x in range(m) and y in range(n) and visited[x][y] == False):
			print('x, y:', x, '-', y, '-condtion :',cnt_condition)
			if( grid[x][y] == 0 or (grid[x][y] == 2 and cnt_condition == 0) ):
				visited[x][y] = True
				dfs(visited, grid, (x,y), pos_end, cnt_condition-1, cnt_obstacle, rst,dx, dy, m ,n)
				visited[x][y] = False
				# cnt_condition +=1
						 
				 
				
if __name__ =='__main__':
		grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
		pos_start, pos_end, cnt_condition, cnt_obstacle = (-1,-1),(-1,-1),0, 0
		m = len(grid)
# 		if m ==0 : return 0
		n = len(grid[0])
# 		if n == 0: return 0
		for i in range(m):
			for j in range(n):
				if(grid[i][j]== 0):
					cnt_condition +=1
				elif(grid[i][j] == 1):
					pos_start = (i,j)
				elif(grid[i][j] == 2):
					pos_end = (i,j)
				else:
					cnt_obstacle += 1 
# 		if( pos_start[0]==-1  or pos_end[0]==-1  ):
# 			return 0 
		print(pos_start)
		print(pos_end)
		visited = [[False for i in range(n)] for j in range(m)]		
		rst= []
		dx, dy = [0,0,-1, 1],[-1,1,0,0]
		visited[pos_start[0]][pos_start[1]]= True
		dfs(visited, grid, pos_start, pos_end, cnt_condition, cnt_obstacle, rst,dx,dy,m ,n)
		print(rst)
		print(len(rst))