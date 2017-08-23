#Uses python3
#Output the 2-SAT solver:
import sys

def read_graph():
    n, e = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(e) ]
    Adj= {}
    for u in range(2*n):
        Adj[u] = set([])
    
    for (a,b) in clauses:
        if a== b:
            if a >= 0:
                Adj[n + a - 1].add(a - 1)
            else:
                Adj[-a - 1].add(n -a -1)
            continue
        if a >= 0:
            if b >= 0:
                Adj[n + a - 1].add(b-1)
                Adj[n + b - 1].add(a-1)
            else:
                Adj[n + a - 1].add(n - b - 1)
                Adj[-b - 1].add(a-1)
        else:
            if b >= 0:
                Adj[- a - 1].add(b - 1)
                Adj[n + b - 1].add(n - a - 1)
            else:
                Adj[- a - 1].add(n - b - 1)
                Adj[- b - 1].add(n - a - 1)
    print(Adj)
    return Adj

def reverse_graph(adjacent_lists):
    reversed_adjacent_lists = {}
    for u in adjacent_lists:
        reversed_adjacent_lists[u] = set()
    for u in adjacent_lists:
        for v in adjacent_lists[u]:
            reversed_adjacent_lists[v].add(u)
    return reversed_adjacent_lists

def scc(G):
    GT = reverse_graph(G)
    print(GT)
    sccs, seen = [], set()
    for u in iter_dfs_topsort(GT):
        if u in seen:
            continue
        C = walk(G, u, seen)
        seen.update(C)
        sccs.append(C)
    #print(seen)
    print(sccs)
    return sccs

def iter_dfs_topsort(G):
    print(G)
    S, Q, res = set(), [], []
    for u in G:
        Q.append(u)
        while Q:
            v = Q.pop()
            print(S, u)
            if u in S:
                continue
            S.add(v)
            Q.extend(G[v])
            #print(v, G[v])
            #print('append(u)', u)
        res.append(u)
    res.reverse()
    return res
def walk(G, s, S = set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            Q.add(v)
            P[v]  = u
    return P

        
def main():
    result = scc(read_graph())

if __name__ == '__main__':
    main()
