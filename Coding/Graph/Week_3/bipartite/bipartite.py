#Uses python3
#Check whether or not a graph is bipartite:
import sys
import queue

def bipartite(adj):
    #print(adj)
    for i in range(len(adj)):
        for t in adj[i]:
            if t == i:
                return 0
    #write your code here
    prev = [-1]*len(adj)
    dist = [-1]*len(adj)
    
    for s in range(len(adj)):
        if dist[s] != -1:
            continue
        #print(s)
        dist[s] = 0
        prev[s] = s
        Q = [s]
        while len(Q) != 0:
            u = Q.pop(0)
            for v in adj[u]:
                #Check if 2 adjacent vertices has the same color (dis[v] - dis[u] %2 = 0) 
                if dist[v] != -1 and (dist[v] - dist[u])%2 == 0:
                    return 0
                elif dist[v] == -1:
                    Q.append(v)
                    dist[v] = dist[u] + 1
                    prev[v] = u
    return 1

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
        adj[b - 1].append(a - 1)
    if n == 1 or m == 0:
        print(0)
    else:
        print(bipartite(adj))
