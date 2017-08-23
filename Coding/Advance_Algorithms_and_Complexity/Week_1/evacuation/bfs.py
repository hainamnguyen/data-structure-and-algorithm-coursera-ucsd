#Uses python3

import sys
import queue

def distance(adj, s, t):
    dist = [[-1]for i in range(len(adj))]
    dist[s][0] = 0
    #print(dist)
    Q = [s]
    while len(Q) != 0:
        u = Q.pop(0)
        for adj_cou in adj[u]:
            #print(adj_cou)
            #print(dist[adj_cou][0])
            if dist[adj_cou][0] == -1:
                Q.append(adj_cou)
                dist[adj_cou][0] = dist[u][0] + 1
                try:
                    dist[adj_cou] += dist[u][1:]
                    dist[adj_cou].append(u)
                except:
                    dist[adj_cou].append(u)
    #write your code here
    return dist[t] + [t]

if __name__ == '__main__':
    #input = sys.stdin.read()
    data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
