# python3
import time
import sys
INF = 1000000000

best_cost = 0

def reduce(size, w, row, col, rowred, colred):
    rvalue = 0
    for i in range(size):
        temp = INF
        for j in range(size):
            temp = min(temp, w[row[i]][col[j]])
        if temp > 0:
            for j in range(size):
                if w[row[i]][col[j]] < INF:
                    w[row[i]][col[j]] -= temp
            rvalue += temp
        rowred[i] = temp
    for j in range(size):
        temp = INF
        for i in range(size):
            temp = min(temp, w[row[i]][col[j]])
        if temp > 0:
            for i in range(size):
                if w[row[i]][col[j]] < INF:
                    w[row[i]][col[j]] -= temp
            rvalue += temp
        colred[j] = temp
    return rvalue


def bestEdge(size, w, row, col):
    mosti = -INF
    ri = 0
    ci = 0
    for i in range(size):
        for j in range(size):
            if not w[row[i]][col[j]]:
                minrowwelt = INF
                zeroes = 0
                for k in range(size):
                    if not w[row[i]][col[k]]:
                        zeroes += 1
                    else:
                        minrowwelt = min(minrowwelt, w[row[i]][col[k]])
                if zeroes > 1: minrowwelt = 0
                mincolwelt = INF
                zeroes = 0
                for k in range(size):
                    if not w[row[k]][col[j]]:
                        zeroes += 1
                    else:
                        mincolwelt = min(mincolwelt, w[row[k]][col[j]])
                if zeroes > 1: mincolwelt = 0
                if minrowwelt + mincolwelt > mosti:
                    mosti = minrowwelt + mincolwelt
                    ri = i
                    ci = j
    return mosti, ri, ci


def explore(n, w, edges, cost, row, col, best, fwdptr, backptr):
    global best_cost

    colred = [0 for _ in range(n)]
    rowred = [0 for _ in range(n)]
    size = n - edges
    cost += reduce(size, w, row, col, rowred, colred)
    if cost < best_cost:
        if edges == n - 2:
            for i in range(n): best[i] = fwdptr[i]
            if w[row[0]][col[0]] >= INF:
                avoid = 0
            else:
                avoid = 1
            best[row[0]] = col[1 - avoid]
            best[row[1]] = col[avoid]
            best_cost = cost
        else:
            mostv, rv, cv = bestEdge(size, w, row, col)
            lowerbound = cost + mostv
            fwdptr[row[rv]] = col[cv]
            backptr[col[cv]] = row[rv]
            last = col[cv]
            while fwdptr[last] != INF: last = fwdptr[last]
            first = row[rv]
            while backptr[first] != INF: first = backptr[first]
            colrowval = w[last][first]
            w[last][first] = INF
            newcol = [INF for _ in range(size)]
            newrow = [INF for _ in range(size)]
            for i in range(rv): newrow[i] = row[i]
            for i in range(rv, size - 1): newrow[i] = row[i + 1]
            for i in range(cv): newcol[i] = col[i]
            for i in range(cv, size - 1): newcol[i] = col[i + 1]
            explore(n, w, edges + 1, cost, newrow, newcol, best, fwdptr, backptr)
            w[last][first] = colrowval
            backptr[col[cv]] = INF
            fwdptr[row[rv]] = INF
            if lowerbound < best_cost:
                w[row[rv]][col[cv]] = INF
                explore(n, w, edges, cost, row, col, best, fwdptr, backptr)
                w[row[rv]][col[cv]] = 0

    for i in range(size):
        for j in range(size):
            w[row[i]][col[j]] = w[row[i]][col[j]] + rowred[i] + colred[j]


def atsp(w):
    global best_cost
    size = len(w)
    col = [i for i in range(size)]
    row = [i for i in range(size)]
    best = [0 for _ in range(size)]
    route = [0 for _ in range(size)]
    fwdptr = [INF for _ in range(size)]
    backptr = [INF for _ in range(size)]
    best_cost = INF

    explore(size, w, 0, 0, row, col, best, fwdptr, backptr)

    index = 0
    for i in range(size):
        route[i] = index
        index = best[index]
    index = []
    cost = 0

    for i in range(size):
        if i != size - 1:
            src = route[i]
            dst = route[i + 1]
        else:
            src = route[i]
            dst = 0
        cost += w[src][dst]
        index.append([src, dst])
    return cost, index


def main():
    # adjasted matrix
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    #print(graph)
    '''
    graph = [[INF,   29  ,20  ,21 , 16 , 31,  100 ,12,  4 ,  31 ,18],
             [29,  INF ,  15 , 29,  28 , 40 , 72,  21  ,29,  41 , 12],
             [20 , 15 , INF  , 15  ,14,  25,  81,  9   ,23 , 27  ,13],
             [21, 29 , 15 , INF  , 4 ,  12  ,92  ,12  ,25 , 13 , 25],
             [16, 28  ,14 ,4   ,INF ,  16,  94 , 9,   20  ,16 , 22],
             [31  ,40 , 25  ,12 , 16,  INF ,  95 ,24 , 36 , 3 ,  37],
              [100, 72 , 81  ,92 , 94 , 95 , INF,   90 , 101 ,99,  84],
              [12 , 21  ,9  , 12,  9  , 24 , 90,  INF ,  15,  25 , 13],
              [4  , 29,  23  ,25 ,20  ,36 , 101, 15 , INF  , 35 , 18],
             [31 , 41  ,27 , 13  ,16,  3  , 99  ,25, 35,  INF  , 38],
                 [18 ,12  ,13 , 25  ,22  ,37  ,84  ,13 , 18 ,38,  INF]]
                 '''
    start_time = time.time()
    cost, path = atsp(graph)
    if cost > INF:
        print(-1)
        sys.exit()
    print (cost)
    result = []
    for i in path:
        result.append(str(i[0] + 1))
    print(" ".join(result))
    #print ("Time (s)", time.time() - start_time)

if __name__ == "__main__":
    main()
