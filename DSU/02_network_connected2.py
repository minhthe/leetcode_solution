'''
https://leetcode.com/problems/number-of-operations-to-make-network-connected/

***Using DFS
AC in the second time (21 minutes)

***Complexity: 
Time :O(E+V) -> O(n+ m ) (m is lengthe connetions)
Space : O(n)
'''

#wrong in set assign visited -> TLE with BFS
#set 2 points: 
#point 1: from the instantiate stk
#point 2: from the append stk
def dfs(point, graph, visited):
    stk = [point]
    while(len(stk)):
        u = stk.pop() 
        visited[u] = True
        for adj in graph[u]:
            if(visited[adj] is False):
                stk.append(adj)
    
class Solution(object):
    def makeConnected(self, n, connections):
        current = len(connections)
        if(current == 0 or n - current > 1 or n == 0):
            return -1 
        cnt = 0
        visited = [False for i in range(n)]
        graph = [[] for i in range(n) ]
        for edge in connections:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)
            
        for i in range(n):
            if(visited[i] is False):
                dfs(i, graph, visited)
                cnt +=1
                
        return cnt - 1