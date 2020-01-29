'''
*** using BFS

***best practice:
#wrong in set assign visited -> TLE with BFS
#set 2 points: 
#point 1: from the instantiate stk  
#point 2: from the append stk

'''
import Queue as queue
def bfs(point, graph, visited):
    que= queue.Queue()
    que.put(point)
    while( not que.empty()  ):
        u = que.get()
        visited[u] = True
        for adj in graph[u]:
            if(visited[adj] is False):
                visited[adj] = True
                que.put(adj)
    
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
                bfs(i, graph, visited)
                cnt +=1
                
        return cnt - 1