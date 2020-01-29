'''
9
1 2 1
2 3 1
4 5 1
5 6 1
2 6 2
6 7 1
7 3 1
6 2 2
7 1 2

Union by rank and path compression:




'''
path = []
rank = []
def makeSet(n):
  global path, rank
  path = [i for i in range(n+5)]
  rank = [0 for i in range(n+5)]

def findSet(u):
  if(path[u]!= u):
    path[u] = findSet(path[u] )
  return path[u]

def unionSet(u,v):
  pu = findSet(u)
  pv = findSet(v)
  if(pu==pv):
    return
  elif( rank[pu] > rank[pv] ):
    path[pv] = pu
  elif(rank[pu] < rank[pv]) :
    path[pu] = pv
  else:
    path[pu] = pv
    rank[pv] += 1 

if __name__ == '__main__':
  n = int(input())
  makeSet(50)
  for _ in range(n):
    u, v ,p = map(int , input().split())
    if(p == 1):
      unionSet(u ,v)
    else:
      pu = findSet(u)
      pv = findSet(v)
      if(pu != pv):
        print('False')
      else:
        print('True')
