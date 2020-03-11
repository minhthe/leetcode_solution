'''
https://leetcode.com/problems/time-needed-to-inform-all-employees
'''
from queue import Queue
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for i in range(n)]
        for i,v in enumerate(manager):
            if v != -1: graph[v].append(i)
        def bfs(graph, n , headID, manager, informTime):
            q = Queue()
            q.put((headID, informTime[headID]))
            rst = informTime[headID]
            while(q.empty() is False):
                u,v = q.get()
                for adj in graph[u]:

                    rst = max(rst, v + informTime[adj])
                    q.put((adj, v + informTime[adj]))
            return rst
                
            
        return bfs(graph, n , headID, manager, informTime)
        