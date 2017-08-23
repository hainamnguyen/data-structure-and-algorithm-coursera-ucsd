# python3
import sys

def PreprocessBWT(bwt):
  starts = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0, '$': 0}
  occ_count_before = {'A' : [0], 'C' : [0], 'G' : [0], 'T' : [0], '$' : [0]}
  sortedBwt = sorted(bwt)
  for i in starts:
    try:
      starts[i] = sortedBwt.index(i)
    except:
      starts[i] = float('inf')
      continue
    count_before = 0
    for j in range(1, len(bwt) + 1):
      if i == bwt[j-1]:
        count_before += 1
      occ_count_before[i].append(count_before)
  #print(starts)
  #print(occ_count_before)
  return starts, occ_count_before


def suffix_array_matching(pattern, bwt, starts, occ_counts_before, suffix_array):
  pattern = list(pattern[::-1])
  top = 0
  bottom = len(bwt) - 1
  while top <= bottom:
    if len(pattern) != 0:
      symbol = pattern.pop(0)
      #print(symbol)
      if symbol in bwt[top : bottom +1]:
        top = starts[symbol] + occ_counts_before[symbol][top]
        bottom = starts[symbol] + occ_counts_before[symbol][bottom + 1] -1
      else:
        return {}
    else:
      return set(suffix_array[top:bottom +1])
def build_suffix_array(S):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  order = SortCharacters(S)
  class_ = ComputeCharClasses(S, order)
  L = 1
  while L < len(S):
    order = SortDoubled(S , L , order , class_)
    class_ = UpdateClasses(order , class_ , L)
    L = 2*L
  return order

def SortCharacters(S):
  sufiixList = []
  
  for i in range(len(S)):
    sufiixList.append([S[i],i])
  #print(sufiixList)
  sufiixList.sort()
  
  return [i[1] for i in sufiixList]

def ComputeCharClasses(S, order):
  lenOfS = len(S)
  class_ = [[]] * lenOfS
  class_[order[0]] = 0
  
  for i in range(1,lenOfS):
    if S[order[i]] != S[order[i-1]]:
      class_[order[i]] = class_[order[i - 1]] + 1
    else:
      class_[order[i]] = class_[order[i-1]]
      
  return class_
def SortDoubled(S, L, order, class_):
  lenOfS = len(S)
  count = [0 for i in range(lenOfS)]
  newOrder = [[] for i in range(lenOfS)]

  for i in range(0, lenOfS):
    count[class_[i]] = count[class_[i]] + 1
  #print(count)
  for j in range(1, lenOfS):
    count[j] = count[j] + count[j - 1]
  #print(count)
  for i in range(lenOfS - 1, -1, -1):
    start = (order[i] - L + lenOfS) % lenOfS
    cl = class_[start]
    count[cl] = count[cl] - 1
    newOrder[count[cl]] = start
    
  return newOrder

def UpdateClasses(newOrder, class_, L):
  n = len(newOrder)
  newClass= [[] for i in range(n)]
  newClass[newOrder[0]] = 0
  #print(newClass)
  for i in range(1, n):
    cur = newOrder[i]
    prev = newOrder[i - 1]
    mid = (cur + L) % n
    midPrev = (prev + L) % n
    if class_[cur] != class_[prev] or class_[mid] != class_[midPrev]:
      temp = newClass[prev] + 1
      newClass[cur] = temp
    else:
      newClass[cur] = newClass[prev]
  return newClass

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  #text = input()
  #pattern_count = int(input())
  #patterns = input().strip().split()
  suffix_array = build_suffix_array(text + '$')
  #print(suffix_array)
  bwt = str()
  for i in suffix_array:
      if i == 0:
          bwt += '$'
      else:
          bwt += text[i - 1]
  #print(bwt)
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = set()
  #print(suffix_array)
  for pattern in patterns:
    occurrence_counts = occurrence_counts.union(suffix_array_matching(pattern, bwt, starts, occ_counts_before, suffix_array))
  print(' '.join(map(str, occurrence_counts)))
