C = 1
n = 0

mymap = {}

nodes = range(1, n + 1)
for i in nodes:
    for j in nodes:
        if i != j:
            mymap[(i, j)] = 0
def varnum(i, j):
    global n
    x =  i * n + j
    global C
    if not x in mymap:
        mymap[x] = C
        C += 1
    return x
n, m = map(int, input().split())
for _ in range(m):
    u, v = map(int, input().split())
    mymap[(u, v)] = 1
    mymap[(v, u)] = 1

print(varnum(30,29))
