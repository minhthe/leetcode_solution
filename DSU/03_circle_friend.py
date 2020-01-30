'''
https://leetcode.com/problems/friend-circles/
AC with 25 minutes

***approach:
DSU with rank and parent compession -> so find_set and untion_set is Log(n)

***edge case:
# the case [[0,0,0],[0,0,0],[0,0,0]] # no one friend with no one(NOT happend)	    # so with this case [[1,0,0],[0,1,0],[0,0,1]] -> at least friend with yourself


***Compexity: N is in range [1,200].
Time: 
 O(n) - whith time loop to make_set
 O(n*n*log(n)) -> whith time travelsal the matrix(n*n) and union_set operation(lo(n)) -> maybe enhane with thes symmetric matrix

Space: 
 O(n) -> create 2 data structure: parent and rank 
'''
def make_set(parent, rank, M, m):
	parent = [i for i in range(m)]
	rank = [0 for i in range(m)]
	return parent , rank

def find_set(u, parent):
	if(parent[u]!= u):
		parent[u] = find_set(parent[u], parent)
	return parent[u]
def union_set(parent, rank, i , j , M):
	pi = find_set(i, parent)
	pj = find_set(j, parent)
	
	if(pi == pj):
		return 
	elif(rank[pi] > rank[pj]):
		parent[pj] = pi

	elif(rank[pi] < rank[pj]):
		parent[pi] = pj

	else:
		parent[pi] = pj
		rank[pj] += 1
		
class Solution(object):
	def findCircleNum(self, M):
		m = len(M)
		if(m == 0): return 0 
		n = len(M[0])
		if(n == 0): return 0 
		
		parent, rank = [], []
		parent, rank = make_set(parent, rank, M , m)
		
		for i in range(m):
			for j in range(n):
				if(M[i][j] == 1):
					union_set(parent, rank, i, j, M)
					
		# for the example [[0,0,0],[0,0,0],[0,0,0]] #no one friend with no one(NOT happend)	       # BUT wrong with this case [[1,0,0],[0,1,0],[0,0,1]] -> at least friend with yourself
		#if(len([i for i in range(m) if rank[i]==0] ) == m): return 0			
		return len([i for i in range(m) if parent[i] == i])