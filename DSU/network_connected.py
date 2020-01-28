'''
https://leetcode.com/problems/number-of-operations-to-make-network-connected/

***log:
AC in first time - 22 minutes

***Noting 
-using union by ranks and parrent compression :
O(log(n)) for operation: find_set, and union_set

***Time complexity:
Time: O(n+m), m is the length of connections
Space: O(n)

'''
parent = []
rank = []

def make_set(n):
    global parent, rank
    parent = [i for i in range(n)]
    rank  = [0 for i in range(n)]
    
def find_set(u):
    if(parent[u] != u):
        parent[u] = find_set(parent[u])
    return parent[u]


def union_set(u, v):
    pu = find_set(u)
    pv = find_set(v)
    if pu == pv : 
        return 
    elif rank[pv] > rank[pu]:
        parent[pu] = pv
    elif rank[pv] < rank[pu]:
        parent[pv] = pu
    else:
        parent[pu] = pv
        rank[pv] += 1
        
class Solution(object):
    def makeConnected(self, n, connections):
        
        current = len(connections)
        if(n == 0 or current == 0 or n - current > 1):
            return -1 
        
        make_set(n)

        for edge in connections:
            u, v = edge[0] , edge[1]
            union_set(u , v)

        cnt_union = len([ i for i in range(len(parent)) if parent[i] == i  ])
        return cnt_union - 1 
        
