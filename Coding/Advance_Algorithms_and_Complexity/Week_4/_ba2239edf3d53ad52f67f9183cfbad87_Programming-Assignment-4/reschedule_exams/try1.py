# python3
import sys
import itertools
import os
import subprocess

n, m = map(int, input().split())
colors = input()
edges = [ list(map(int, input().split())) for i in range(m) ]
# Initialize the neighbourlist:
neighbourList = [[] for i in range(n + 1)]
for i in edges:
    neighbourList[i[0]].append(i[1])
#print(neighbourList)
clauses = []
frequencies = range(1, 4)


def varnum(i, j):
    assert(i in range(1, n + 1) and j in frequencies)
    return 10*i + j

def exactly_one_of(literals):
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])
        
def neighbour(literals):
    #clauses.append([l for l in literals])

    for t in range(1, len(literals)):
        clauses.append([-literals[0], -literals[t]])
        
# cell [i,j] contains exactly one frequency:
for i in range(1, n +1):
    exactly_one_of([varnum(i,j) for j in frequencies])
#print(clauses)
# Neighbouring cells have different frequency:
for i in range(1, n +1):
    try:
        for j in frequencies:
            neighbour([varnum(i,j)] + [varnum(t, j) for t in neighbourList[i]])
    except:
        continue

for i in range(len(colors)):
    if colors[i] == 'R':
       clauses.append([-varnum(i + 1, 1)])
    elif colors[i] == 'G':
       clauses.append([-varnum(i + 1, 2)])
    elif colors[i] == 'B':
       clauses.append([-varnum(i + 1, 3)])
    
#print(clauses)


with open('tmp.cnf', 'w') as f:
    f.write("p cnf {} {}\n".format(999, len(clauses)))
    for c in clauses:
        c.append(0);
        f.write(" ".join(map(str, c))+"\n")

FNULL = open(os.devnull, 'w')
retcode = subprocess.call(['minisat','tmp.cnf', 'tmp.sat'], stdout=FNULL, stderr=subprocess.STDOUT)
result = []
with open("tmp.sat", "r") as satfile:
    for line in satfile:
        if line.split()[0] == "UNSAT":
            print("Impossible")
            sys.exit()
        elif line.split()[0] == "SAT":
            continue
        assignment =  [int(x) for x in line.split()]
        #print(line)
        for i in range(n):
            for j in (frequencies):
                if varnum(i+1, j) in assignment:
                    if j == 1:
                        result.append('R')
                    elif j == 2:
                        result.append('G')
                    else:
                        result.append('B')
        '''
        for i in line.split():
            if int(i) > 0:
                if i[1] =='1':
                    result[int(i[0]) -1] ='R'
                elif i[1] =='2':
                    result[int(i[0]) -1] ='G'
                elif i[1] =='3':
                    result[int(i[0]) -1] ='B'
        '''
print("".join(result))
                


# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.


