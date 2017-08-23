# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
#n, m = map(int, input().split())
#lines = list(map(int, input().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def merge(destination, source):
    Union(source, destination)
    #print(parent)
    #print(lines)
    print(ans)
    
def find(i):
    if i != parent[i]:
        #print(i, parent[i])
        parent[i] = find(parent[i])
    return parent[i]
def Union(i,j):
    i_id = find(i)
    j_id = find(j)
    #print(i_id,j_id)
    if i_id == j_id:
        return
    global ans
    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
        lines[i_id] += lines[j_id]
        ans = max(ans, lines[i_id])
    else:
        parent[i_id] = j_id
        lines[j_id] += lines[i_id]
        ans = max(ans, lines[j_id])
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1
    
    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    
