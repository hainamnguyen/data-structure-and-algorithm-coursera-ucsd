import queue as Q

line = input()

array = [i for i in line.split()]
n = int(array[0])
m = int(array[1])

if n == 0 or m == 0:
    print(0)
    exit()
graph = {}
seen = {}



infinity = float("inf")

visited = [False] * (n + 1)
distance = [infinity] * (n + 1)
dist = infinity

#build
for i in range(1, n+1):
    graph[i] = set()



for i in range(m):
    u, v, w = map(int, input().split())
    if u == v and w >= 0:
        continue
    # edges from u are not in dictionary yet
    if u not in graph:
        graph[u].add((v, w))
        seen[(u, v)] = w
    # there are edges from u in graph
    else:
        # an edge from u to v was already introduced
        if (u, v) in seen:
            # check whether the new edge from u to v is shorter, if yes, replace the old one
            if w < seen[(u, v)]:
                graph[u].remove((v, seen[(u, v)]))
                graph[u].add((v, w))
                seen[(u, v)] = w
        # an edge from u to v has not been introduced
        else:
            graph[u].add((v, w))
            seen[(u, v)] = w



def BellmanFord():
    for j in range(n-1):
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    global change
                    change = True
                if distance[u] == infinity and distance[v] != infinity:
                    distance[u] = distance[v] - weight



print(u)
distance[u] = 0
BellmanFord()



change = False
result = 0
for u in graph:
    for v, weight in graph[u]:
        if distance[u] + weight < distance[v]:
            distance[v] = distance[u] + weight
            change = True
if change:
    result = 1
print(result)
