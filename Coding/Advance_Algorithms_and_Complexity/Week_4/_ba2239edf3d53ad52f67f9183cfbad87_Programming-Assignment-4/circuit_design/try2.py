#Uses python3
#Output the 2-SAT solver:
import sys
import threading
sys.setrecursionlimit(10**6)
threading.stack_size(2**26) 

def read_graph():
    n, e = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(e) ]
    Adj= [[] for _ in range(2  *n)]
    for (a,b) in clauses:
        if a== b:
            if a >= 0:
                Adj[n + a - 1].append(a - 1)
            else:
                Adj[-a - 1].append(n -a -1)
            continue
        if a >= 0:
            if b >= 0:
                Adj[n + a - 1].append(b-1)
                Adj[n + b - 1].append(a-1)
            else:
                Adj[n + a - 1].append(n - b - 1)
                Adj[-b - 1].append(a-1)
        else:
            if b >= 0:
                Adj[- a - 1].append(b - 1)
                Adj[n + b - 1].append(n - a - 1)
            else:
                Adj[- a - 1].append(n - b - 1)
                Adj[- b - 1].append(n - a - 1)
    print(Adj)
    return Adj
def reverse_graph(adjacent_lists):
    reversed_adjacent_lists = [[] for _ in range(len(adjacent_lists))]
    for from_v in range(len(adjacent_lists)):
        for to_v in adjacent_lists[from_v]:
            reversed_adjacent_lists[to_v].append(from_v)
    return reversed_adjacent_lists
#We need to replace recursion in the following function:
def search(adjacent_lists, visited, leave_sequences, v):
    visited[v] = True
    for adj in adjacent_lists[v]:
        if not visited[adj]:
            search(adjacent_lists, visited, leave_sequences, adj)
    leave_sequences.append(v)

def dfs(adjacent_lists, sources=None):
    if sources == None:
        sources = range(len(adjacent_lists))
    
    visited = [False] * len(adjacent_lists)
    leave_sequences = []
    for source in sources:
        if not visited[source]:
            search(adjacent_lists, visited, leave_sequences, source)
    return leave_sequences
#We need to replace recursion in the following function:
def search_sat(adjacent_lists, visited, v, tree_num, tree_group):
    visited[v] = True
    tree_group[v] = tree_num
    for adj in adjacent_lists[v]:
        if not visited[adj]:
            search_sat(adjacent_lists, visited, adj, tree_num, tree_group)

    
def dfs_sat(adjacent_lists, sources):
    number_of_vertices = len(adjacent_lists)
    visited = [False] * number_of_vertices
    tree_group = [0] * number_of_vertices
    tree_num = 0
    for source in sources:
        if not visited[source]:
            search_sat(adjacent_lists, visited, source, tree_num, tree_group)
            tree_num += 1
            #print(tree_group)
    return tree_group


def find_strongly_connected_components(adjacent_lists):
    number_of_vertices = len(adjacent_lists)
    n = int((number_of_vertices)/2)
    leave_sequences = dfs(reverse_graph(adjacent_lists))
    print(leave_sequences)
    tree_group = dfs_sat((adjacent_lists), leave_sequences[::-1])
    for i in range(n):
        if tree_group[i] == tree_group[i +n]:
            return "UNSATISFIABLE"
    print(tree_group)    
    tree_group = sorted(range(number_of_vertices), key=lambda k: tree_group[k])
    print('tree_group', tree_group)
    satList = [False]  * n
    for i in tree_group:
        if i <= n-1 and satList[i] == 0:
            satList[i] = i + 1
        elif i > n-1 and satList[i - n] == 0:
            satList[i - n] = n - i - 1
    return satList
        
def main():
    result = find_strongly_connected_components(read_graph())
    if result == "UNSATISFIABLE":
        print(result)
    else:
        print('SATISFIABLE')
        print(*result, sep=' ')

if __name__ == '__main__':
    main()
