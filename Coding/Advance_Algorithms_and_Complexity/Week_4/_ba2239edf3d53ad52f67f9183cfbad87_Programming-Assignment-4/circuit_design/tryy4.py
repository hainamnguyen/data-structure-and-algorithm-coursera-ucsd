#Uses python3
def read_graph():
    n, e = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(e) ]
    Adj= {}
    for u in range(1, 2*n+ 1):
        Adj[u] = []
    for (a,b) in clauses:
        if a== b:
            if a >= 0:
                Adj[n + a].append(a)
            else:
                Adj[-a].append(n -a)
            continue
        if a >= 0:
            if b >= 0:
                Adj[n + a].append(b)
                Adj[n + b].append(a)
            else:
                Adj[n + a].append(n - b)
                Adj[-b].append(a)
        else:
            if b >= 0:
                Adj[- a ].append(b)
                Adj[n + b].append(n - a)
            else:
                Adj[- a].append(n - b)
                Adj[- b].append(n - a)
    #print(Adj)
    return (n, Adj)

def strongly_connected_components_iterative(n, edges):
    vertices = [i for i in range(2*n)]
    identified = set()
    stack = []
    index = {}
    boundaries = []

    for v in vertices:
        if v not in index:
            to_do = [('VISIT', v)]
            while to_do:
                operation_type, v = to_do.pop()
                if operation_type == 'VISIT':
                    index[v] = len(stack)
                    stack.append(v)
                    boundaries.append(index[v])
                    to_do.append(('POSTVISIT', v))
                    # We reverse to keep the search order identical to that of
                    # the recursive code;  the reversal is not necessary for
                    # correctness, and can be omitted.
                    try:
                        to_do.extend(reversed([('VISITEDGE', w) for w in edges[v]]))
                    except:
                        namdeptrai = "True"
                elif operation_type == 'VISITEDGE':
                    if v not in index:
                        to_do.append(('VISIT', v))
                    elif v not in identified:
                        while index[v] < boundaries[-1]:
                            boundaries.pop()
                else:
                    # operation_type == 'POSTVISIT'
                    if boundaries[-1] == index[v]:
                        boundaries.pop()
                        scc = set(stack[index[v]:])
                        del stack[index[v]:]
                        identified.update(scc)
                        yield scc

def _sat():
    n, adj = read_graph()
    scc = strongly_connected_components_iterative(n, adj)
    satList = [False]  * n
    for i in scc:
        for t in i:
            #print(t)
            if t ==0:
                #print('ww')
                continue
            if t > n:
                if t - n in i:
                    return "UNSATISFIABLE"
                if satList[t -n -1] == 0:
                    satList[t - n - 1] = n - t
                    #print(t, t - n - 1, n - t)
            else:
                if t + n in i:
                    return "UNSATISFIABLE"
                if satList[t -1] == 0:
                    satList[t - 1] = t
                    #print(t, t - 1, t)
    return satList
            

def main():
    result = _sat()
    if result == "UNSATISFIABLE":
        print(result)
    else:
        print('SATISFIABLE')
        print(*result, sep=' ')
if __name__ == '__main__':
    main()
'''
#scc = list((strongly_connected_components_iterative([1, 2, 3, 4, 5, 6, 7, 8], {1: [2], 2: [3, 8], 3: [4, 7], 4: [5], 5: [3, 6], 6: [], 7: [4, 6], 8: [1, 7]})))

#for i in scc:
#    print((i))
#{1: [2, 3], 2: [3, 4], 3: [], 4: [3, 5], 5: [2, 6], 6: [3, 4]}
#{1: [2], 2: [6], 3: [1, 4], 4: [5], 5: [3], 6: []}
#[[1], [5], [0, 4], [5], [3], []]

vertices = [1, 2, 3, 4, 5, 6]
edges = {1: [2, 3], 2: [3, 4], 3: [], 4: [3, 5], 5: [2, 6], 6: [3, 4]}
for scc in strongly_connected_components_iterative(vertices, edges):
    print(scc)
'''
