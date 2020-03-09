'''
https://leetcode.com/problems/time-needed-to-inform-all-employees/
'''
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = [[] for i in range(n)]
        
        for i,v in enumerate(manager):
            if v != -1: graph[v].append(i)
        
        def dfs(graph, n, headID, manager, informTime)       :
            stk = [(headID, informTime[headID])]
            rst = 0
            while(len(stk)):
                u, v = stk.pop()
                for adj in graph[u]:
                    rst = max(rst, v+ informTime[adj])
                    stk.append( (adj, v+ informTime[adj]) )
            return rst
                    
                    
            
        rst = dfs(graph, n, headID, manager, informTime)        
        return rst
        
        