#Uses python3
# Finding an Exit from a Maze
#Test case 1: 4 4 1 2 3 2 4 3 1 4 1 4
#Test case 2: 4 2 1 2 3 2 1 4

import sys         
def reach(adj, x, y):
    def explore(adj, visitedList, v):
        visitedList[v] = 1
        for i in adj[v]:
            if visitedList[i] == 0:
                visitedList = explore(adj, visitedList, i)
        return visitedList
    
    visitedList = [0 for i in range(len(adj))]
    visitedList = explore(adj, visitedList, x)
    
    return visitedList[y]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
        
    print(reach(adj, x, y))
