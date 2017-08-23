# python3
from sys import stdin
import numpy as np
import itertools
def solve_diet_problem(n, m, A, b, c):  
  numOfEquations = len(A)
  equationGroups = list(itertools.combinations([i for i in range(n + m)], m))
  maxValue = -float('inf')
  ansx = np.array([])
  
  for i in equationGroups:
    linearMatrix1 = []
    linearMatrix2 = []
    for j in i:
      linearMatrix1.append(A[j])
      linearMatrix2.append(b[j])
    try:
      x = np.linalg.solve(np.array(linearMatrix1), np.array(linearMatrix2))
    except:
      continue
    prerequisite = True
    for k in range(numOfEquations):
      if k in i or sum(x * np.array(A[k])) <= b[k]:
        continue
      else:
        prerequisite = False
        break
    if prerequisite == False:
      continue
    value = sum(x * np.array(c))
    if value > maxValue:
      maxValue = value
      ansx = x
  return list(ansx)

def solve_diet_problem_check(n, m, A, b, c, ansx):  
  numOfEquations = len(A)
  equationGroups = list(itertools.combinations([i for i in range(n + m)], m))
  maxValue = sum(np.array(ansx) * np.array(c))

  for i in equationGroups:
    if numOfEquations - 1 not in i:
      continue
    linearMatrix1 = []
    linearMatrix2 = []
    for j in i:
      linearMatrix1.append(A[j])
      linearMatrix2.append(b[j])
    try:
      x = np.linalg.solve(np.array(linearMatrix1), np.array(linearMatrix2))
    except:
      continue
    prerequisite = True
    for k in range(numOfEquations):
      if k in i or sum(x * np.array(A[k])) <= b[k]:
        continue
      else:
        prerequisite = False
        break
    if prerequisite == False:
      continue
    
    value = sum(x * np.array(c))
    if value > maxValue:
      maxValue = value
      ansx = x
  return list(ansx)

n, m = list(map(int, input().split()))
A = []
for i in range(m):
  unit_vector = [0 for i in range(m)]
  unit_vector[i] = -1
  A.append(unit_vector)
for i in range(n):
  A += [list(map(int, input().split()))]
b = [0 for i in range(m)] + list(map(int, input().split()))
c = list(map(int, input().split()))
ACheck = A + [[1 for i in range(m)]]
bCheck = b + [10**9]
ansx = solve_diet_problem(n, m, A, b, c)
anst = 0
if len(ansx) == 0:
  anst = -1
elif ansx != solve_diet_problem_check(n + 1, m, ACheck, bCheck, c, ansx):
  anst = 1
if anst == -1:
  print("No solution")
if anst == 0:  
  print("Bounded solution")
  for row in range(len(ansx)):
        ansx[row] = "%.20lf" % ansx[row]
  print(*ansx, sep=' ')
if anst == 1:
  print("Infinity")
    
