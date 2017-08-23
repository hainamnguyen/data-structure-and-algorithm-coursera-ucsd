# Uses python3
# Number of connected components
#  Test case: 4 2 1 2 3 2
import sys

def number_of_components(adj):
    def explore(adj, visitedList, v):
        visitedList[v] = 1
        for i in adj[v]:
            if visitedList[i] == 0:
                visitedList = explore(adj, visitedList, i)
        return visitedList

    visitedList = [0 for i in range(len(adj))]
    result = 0
    
    for i in range(len(adj)):
        if visitedList[i] == 0:
            visitedList = explore(adj, visitedList, i)
            result += 1
            
    return result

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
        
    print(number_of_components(adj))
