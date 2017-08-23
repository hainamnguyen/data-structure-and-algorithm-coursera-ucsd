#Uses python3

import sys

def negative_cycle(adj):
    #write your code here
    number_of_V = len(adj)
    t = float('inf')
    dist = [t] * number_of_V
    prev = [-1] * number_of_V
    for i in range(number_of_V):
        if adj[i] != []:
            dist[i] = 0
    for i in range(number_of_V - 1):
        for source in range(number_of_V):
            for destination in adj[source]:
                if dist[destination[0]] > dist[source] + destination[1]:
                    dist[destination[0]] = dist[source] + destination[1]

    for source in range(number_of_V):
        for destination in adj[source]:
            if dist[destination[0]] > dist[source] + destination[1]:
                return 1
    return 0

if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    adj = [[] for _ in range(n)]
    
    for ((a, b), w) in edges:
        adj[a - 1].append([(b - 1), w])
    #print(adj)
    print(negative_cycle(adj))
