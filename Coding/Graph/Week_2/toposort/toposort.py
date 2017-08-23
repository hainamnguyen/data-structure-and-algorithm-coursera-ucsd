#Uses python3
#Output any topological ordering of its vertices.
#Test case 1: 4 4 1 2 4 1 2 3 3 1
#Test case 2: 5 7 1 2 2 3 1 3 3 4 1 4 2 5 3 5
import numpy as np
import sys
sys.setrecursionlimit(200000)   
    
class graph:
    def __init__(self, adj):
        self.SCCgroup = [0 for i in range(len(adj))]
        self.order = []
        self.post = [0 for i in range(len(adj))]
        self.visitedList = [0 for i in range(len(adj))]
        self.clockWise = 0
        self.adj = adj
        
    def explore(self, v):
        self.visitedList[v] = 1
        self.clockWise += 1
        for i in self.adj[v]:
            if self.visitedList[i] == 0:
                self.explore(i)
        self.post[v] = self.clockWise
        self.clockWise += 1
        
    def DFS_postoder(self):
        for i in range(len(adj)):
            if self.visitedList[i] == 0:
                self.explore(i)
                
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        
    t = graph(adj)
    t.DFS_postoder()
    resultReserveArray = np.array(t.post)
    resultArray = arr.argsort()[::-1]
    print(*ind + 1, sep = ' ')
