#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []

def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def fun_party(tree, v, parent, D, visited):
    #print(visited)
    visited.add(v)
    m1 = 0
    m0 = 0
    if D[v] == float('inf'):
        #print('v, parent' , v, parent)
        if len(tree[v].children) == 1 and tree[v].children[0] == parent:
            D[v] = tree[v].weight
        else:
            for u in tree[v].children:
                #print('vong 2', v, u)
                if u == v or u in visited:
                    continue
                else:
                    m0 = m0 + fun_party(tree,u,v,D, visited)
            m1 = tree[v].weight
            #print(m1)
            
            for u in tree[v].children:
                #print('vong 1', v, u)
                if u == v or u in visited:
                    continue
                else:
                    for w in tree[u].children:
                        if w == u or w in visited:
                            continue
                        else:
                            #print(w,u)
                            #print( tree[v].children[0] , parent, len(tree[v].children))
                            m1 = m1 + fun_party(tree, w, u, D, visited)
            
            D[v] = max(m1, m0)
    #print('D', D)
    visited.remove(v)
    return D[v]

    # This is a template function for processing a tree using depth-first search.
    # Write your code here.
    # You may need to add more parameters to this function for child processing.


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    visited = set()
    if size == 0:
        return 0
    D = [float('inf')] * len(tree)
    v = -1
    for i in range(len(tree)):
        if len(tree[i].children) == 1:
            v = i
            break
    # You must decide what to return.
    return fun_party(tree, v, -1, D, visited)

def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)
    
#main()

# This is to avoid stack overflow issues
threading.Thread(target=main).start()
