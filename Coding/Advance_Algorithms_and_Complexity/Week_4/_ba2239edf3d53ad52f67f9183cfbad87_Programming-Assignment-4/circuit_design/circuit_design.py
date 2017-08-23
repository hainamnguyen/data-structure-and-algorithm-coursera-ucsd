# python3
import sys
sys.setrecursionlimit(2000000)   
    
class graph:
    def __init__(self, adj):
        self.SCCgroup = [0 for i in range(len(adj))]
        self.post = [0 for i in range(len(adj))]
        self.visitedList = [0 for i in range(len(adj))]
        self.clockWise = 0
        self.adj = adj
        self.SCCnumber = {}
        self.SCCclock = 0
        
    def explore(self, v):
        self.visitedList[v] = 1
        self.clockWise += 1
        #print(v)
        for i in self.adj[v]:
            if self.visitedList[i] == 0:
                self.explore(i)
        self.post[v] = self.clockWise
        self.clockWise += 1
        
    def explore_SCC(self, v, adj):
        #print(v)
        self.visitedList[v] = 1
        self.SCCgroup[v] = 0
        self.SCCnumber[v] = self.SCCclock
        #print(v)
        #print(self.visitedList)
        for i in adj[v]:
            if self.visitedList[i] == 0:
                self.explore_SCC(i, adj)
                
    def DFS_postoder(self):
        for i in range(len(self.adj)):
            if self.visitedList[i] == 0:
                self.explore(i)
        #print(self.post)
    def acyclic(self,postOrder, adj):
        numberOfSCC = 0
        # Reset the visted list to use for the main graph:
        self.visitedList = [0 for i in range(len(self.adj))]
        self.SCCgroup = postOrder
        #print(postOrder)
        
        while max(self.SCCgroup) != 0:
           # print(self.SCCgroup)
            i = self.SCCgroup.index(max(self.SCCgroup))
            self.explore_SCC(i, adj)
            self.SCCclock += 1
            numberOfSCC += 1
        #print(numberOfSCC)
        #print(self.SCCnumber)
        for i in range(n):
            if self.SCCnumber[i] == self.SCCnumber[i + n]:
                return "UNSATISFIABLE"
        satList = [0 for i in range(n)]
        #print(len(satList))
        sortedSCCnumber = sorted(self.SCCnumber, key = self.SCCnumber.get)
        #print(sortedSCCnumber)
        for i in sortedSCCnumber:
            #print(i, n-1, i - n + 1)
            if i <= n-1 and satList[i] == 0:
                satList[i] = i + 1
            elif i > n-1 and satList[i - n] == 0:
                satList[i - n] = n - i - 1
                #print(n-i-1)

        return satList
                    
n, m = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(m) ]
reversedAdj= [[] for _ in range(2*n)]
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
for i in range(len(reversedAdj)):
    for j in reversedAdj[i]:
        adj[j].append(i)
        
#print(reversedAdj)
#print(adj)
#print(len(adj))
t = graph(reversedAdj)
t.DFS_postoder()
result = t.acyclic(t.post, adj)
if result == "UNSATISFIABLE":
    print(result)
else:
    print('SATISFIABLE')
    print(*result, sep=' ')

