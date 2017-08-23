# python3
import sys
sys.setrecursionlimit(2000000)

#Input and create neighbour list:
n, m = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(m) ]
reversedAdj= [[] for _ in range(2  *n)]
for (a,b) in clauses:
    if a== b:
        if a >= 0:
            reversedAdj[a - 1].append(n + a - 1)
        else:
            reversedAdj[n -a -1].append(-a - 1)
        continue
    if a >= 0:
        if b >= 0:
            reversedAdj[b-1].append(n + a - 1)
            reversedAdj[a-1].append(n + b - 1)
        else:
            reversedAdj[n - b - 1].append(n + a - 1)
            reversedAdj[a-1].append(-b - 1)
    else:
        if b >= 0:
            reversedAdj[b - 1].append(- a - 1)
            reversedAdj[n - a - 1].append(n + b - 1)
        else:
            reversedAdj[n - b - 1].append(- a - 1)
            reversedAdj[n - a - 1].append(- b - 1)
adj = [[] for _ in range(2*n)]
for i in range(2 * n):
    for j in reversedAdj[i]:
        adj[j].append(i)
        
post = [0 for i in range(2 * n)]
visitedList = [0 for i in range(2 * n)]
clockWise = 0
sccNumber = {}

def explore(v):
    global clockWise
    visitedList[v] = 1
    clockWise += 1
    for i in reversedAdj[v]:
        if visitedList[i] == 0:
            explore(i)
    post[v] = clockWise
    clockWise += 1

def DFS_postorder():
    for i in range(2*n):
        if visitedList[i] == 0:
            explore(i)
def explore_SCC(v, sccClock):
    visitedList[v] = 1
    sccNumber[v] = sccClock
    post[v] = 0
    #print(v)
    #print(visitedList)
    for i in adj[v]:
        if visitedList[i] == 0:
            explore_SCC(i, sccClock)

def acyclic():
    numberOfSCC = 0
    sccClock = 0

    while max(post) != 0:
        #print(post)
        i = post.index(max(post))
        explore_SCC(i, sccClock)
        sccClock += 1
        numberOfSCC+= 1
    #print(numberOfSCC)
    #print(sccNumber)
    for i in range(n):
        if sccNumber[i] == sccNumber[i + n]:
            return "UNSATISFIABLE"
    satList = [0 for i in range(n)]
    #sortedSCCnumber = sorted(sccNumber, key = sccNumber.get)
    #print(sortedSCCnumber)
    for i in sorted(sccNumber, key = sccNumber.get):
        if i <= n-1 and satList[i] == 0:
            satList[i] = i + 1
        elif i > n-1 and satList[i - n] == 0:
            satList[i - n] = n - i - 1
    return satList

DFS_postorder()
#print(post)
# Reset the visted list to use for the main graph:
visitedList = [0 for i in range(2 * n)]       
result = acyclic()
if result == "UNSATISFIABLE":
    print(result)
else:
    print('SATISFIABLE')
    print(*result, sep=' ')
