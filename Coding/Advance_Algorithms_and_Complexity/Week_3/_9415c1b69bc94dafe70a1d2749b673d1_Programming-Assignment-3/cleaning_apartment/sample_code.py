# python3
import subprocess
import itertools
import os
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]
# Initialize the neighbourlist:
neighbourList = [[] for i in range(n + 1)]
for i in edges:
    neighbourList[i[0]].append(i[1])
    neighbourList[i[1]].append(i[0])
clauses = []
nodes = range(1, n + 1)
def printEquisatisfiableSatFormula():
    print("Yes")
def printNotEquisttisfiableSatFormula():
    print("No")

def varnum(i, j):
    return n*(i) + j 

#each node j must appear in the path
for j in nodes:
    clauses.append([varnum(i, j) for i in nodes] + [0])
    clauses.append([varnum(j, i) for i in nodes]+ [0])
#no node j appears twice in the path
for (i,k) in itertools.combinations(nodes, 2):
        for j in nodes:
            clauses.append([-varnum(i, j), -varnum(k, j)]+ [0])
            #clauses.append([-varnum(j, i), -varnum(j, k)]) 

#every position i on the path must be occupied
#for i in nodes:
    #clauses.append([varnum(i, j) for j in nodes])
    #clauses.append([varnum(j, i) for j in nodes])
#no two nodes j and k occupy the same postion in the path
for (j,k) in itertools.combinations(nodes, 2):
    for i in nodes:
        clauses.append([-varnum(i, j), -varnum(i, k)]+ [0])
# Non-adjacent nodes i and j cannot be adjacent in the path:
for (i,j) in itertools.product(nodes, repeat = 2):
    if j  not in neighbourList[i]:
        for k in range(1, n):
            clauses.append([-varnum(k, i), -varnum(k + 1, j)]+ [0])
            
with open('tmp.cnf', 'w') as f:
    f.write("p cnf {} {}\n".format(999, len(clauses)))
    for c in clauses:
        f.write(" ".join(map(str, c))+"\n")

FNULL = open(os.devnull, 'w')
retcode = subprocess.call(['minisat','tmp.cnf', 'tmp.sat'], stdout=FNULL, stderr=subprocess.STDOUT)

with open("tmp.sat", "r") as satfile:
   first_line =satfile.readline()
if first_line == "UNSAT\n":
    printNotEquisttisfiableSatFormula()
elif first_line == "SAT\n":
    printEquisatisfiableSatFormula()

