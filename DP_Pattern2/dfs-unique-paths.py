'''
https://leetcode.com/problems/unique-paths


TLE with 
32
12
'''
def dfs(i,j, m,n):
    stk = [(i,j)]
    dx = [1,0]
    dy = [0,1]
    cnt = 0
    while(len(stk)):
        p = stk.pop()
        u, v = p[0], p[1]
        # for special case {m = 1, n = 1}
        if(u== m-1 and v == n-1):
                cnt  +=1
        for i in range(2):
            x, y = dx[i] + u, dy[i] + v
            if(x== m-1 and y == n-1):
                cnt  +=1
            elif(x in range(m) and y in range(n)):
                stk.append( (x,y) )
    return cnt
class Solution(object):
    def uniquePaths(self, m, n):
        if m ==0 or n ==0 : return 0
        
        cnt = 0 
        i, j = 0 ,0
        return dfs(i,j, m,n) 
        