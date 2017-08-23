#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    #print(adj)
    #print(cost)
    dist = [-1]*len(adj)
    prev = [-1]*len(adj)
    dist[s] = 0
    H = [[0,s]]
    while len(H) != 0:
        u = min(H)[1]
        #print(u)
        H.remove(min(H))
        for v in range(len(adj[u])):
            if dist[adj[u][v]] == -1 or dist[adj[u][v]] > dist[u] + cost[u][v]:
                if [dist[adj[u][v]],[adj[u][v]]] in H:
                    H.pop([dist[adj[u][v]],adj[u][v]])
                dist[adj[u][v]] = dist[u] + cost[u][v]
                prev[adj[u][v]] = u                
                H.append([dist[adj[u][v]],adj[u][v]])
    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
