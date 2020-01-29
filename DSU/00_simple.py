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

***intro:
DSU - disjoin set union - this algorith with 3 operitons:
makeSet(), findSet(), unionSet()

Applied in the undirected graph

Union these elements on the graph, IF not find exactly elements, shoud take the Maximun elements

All these 3 operations will take O(n)

'''

parent = []

def makeSet(n):
  global parent
  parent = [i for i in range(n+5)]

def findSet(u):
  while(parent[u] != u):
    u = parent[u]
  return u
def unionSet(u,v):
  pu = findSet(u)
  pv = findSet(v)

  parent[pu] = pv

if __name__ == '__main__':
  operation = int(input())
  makeSet(50)
  for _ in range(operation):
    u, v, o = map(int, input().split())
    if(o == 1):
      unionSet(u,v)
    else:
      pu = findSet(u)
      pv = findSet(v)
      if(pu!= pv):
        print('False')
      else:
        print('True')
       

